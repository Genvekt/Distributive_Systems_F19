from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime

# Prints the local Lamport timestamp and the actual time on the machine 
def local_time(counter):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter,datetime.now())

# Calculates the new timestamp when a process receives a message
def calc_recv_timestamp(recv_time_stamp, counter):
    for id  in range(len(counter)):
        counter[id] = max(recv_time_stamp[id], counter[id])
    return counter


def event(pid, counter):
    counter[pid] += 1
    print('Something happened in {} !'.\
          format(pid) + local_time(counter))
    return counter

def send_message(pipe, pid, counter):
    counter[pid] += 1
    pipe.send(('Empty shell', counter))
    print('Message sent from ' + str(pid) + local_time(counter))
    return counter

def recv_message(pipe, pid, counter):
    counter[pid] += 1
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter)
    print('Message received at ' + str(pid)  + local_time(counter))
    return counter

#a
def process_one(pipe12):
    pid = 0
    counter = [0,0,0]
    # a0
    counter = send_message(pipe12, pid, counter) # a0 - b0
    # a1
    counter = send_message(pipe12, pid, counter) # a1 - b1
    # a2
    counter = event(pid, counter) # a2
    # a3
    counter = recv_message(pipe12, pid, counter) # from b2
    # a4
    counter = event(pid, counter) # a4
    # a5
    counter = event(pid, counter) # a5
    # a6
    counter = recv_message(pipe12, pid, counter) # from b5
    print('Process a ,', counter)

#b
def process_two(pipe21, pipe23):
    pid = 1
    counter = [0,0,0]
    # b0
    counter = recv_message(pipe21, pid, counter) # from a0
    # b1
    counter = recv_message(pipe21, pid, counter) # from a1
    # b2
    counter = send_message(pipe21, pid, counter) # b2 - a3
    # b3
    counter = recv_message(pipe23, pid, counter) # from c0
    # b4
    counter = event(pid, counter) # b4
    # b5
    counter = send_message(pipe21, pid, counter) # b5 - a6
    # b6
    counter = send_message(pipe23, pid, counter) # b6 - c1
    # b7
    counter = send_message(pipe23, pid, counter) # b7 - c3
    print('Process b ,', counter)

#c
def process_three(pipe32):
    pid = 2
    counter = [0,0,0]
    # c0
    counter = send_message(pipe32, pid, counter) # c0 - b3
    # c1
    counter = recv_message(pipe32, pid, counter) # from b6
    # c2
    counter = event(pid, counter) # c2
    # c3
    counter = recv_message(pipe32, pid, counter) # from b7
    print('Process c ,', counter)

if __name__ == '__main__':    
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process1 = Process(target=process_one, 
                       args=(oneandtwo,))
    process2 = Process(target=process_two, 
                       args=(twoandone, twoandthree))
    process3 = Process(target=process_three, 
                       args=(threeandtwo,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
