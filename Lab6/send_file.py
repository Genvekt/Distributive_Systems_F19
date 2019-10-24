import socket
import sys
import os

# define server
SERVER_DOMAIN = 'ec2-18-212-138-166.compute-1.amazonaws.com'
SERVER_PORT = 8800

# define filename
FILE_NAME = sys.argv[1]

# Print file sending progress (taken from elekt.tech)
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

# check the file exists
if not os.path.isfile(FILE_NAME):
    print('ERROR:',FILE_NAME, 'is not in the current derictory.')
    exit()

# connect to server
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
cli_socket.connect((SERVER_DOMAIN,SERVER_PORT))

# define the length of the filename, extend it if needed
name_length = bytes(str(len(FILE_NAME)), 'utf-8')
name_length = (b'0')*(4-len(name_length)) + name_length

# send name length to server
cli_socket.send(name_length)

# send file name to server
cli_socket.send(bytes(FILE_NAME, 'utf-8'))

# define the length of file
file_length = os.path.getsize(FILE_NAME)

# send file 
with open(FILE_NAME,'rb') as f:
    # print enpty progress
    printProgressBar(0, file_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
    data = f.read(512)
    sent = 0
    while data:
        # send data from file
        sent += cli_socket.send(data)
        #print progress
        printProgressBar(sent, file_length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        data = f.read(512)
    # close file  
    f.close()
#close connection
cli_socket.close()
