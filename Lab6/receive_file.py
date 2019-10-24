import socket
from threading import Thread
import os.path

clients = []


# Thread to listen one particular client
class ClientListener(Thread):
    def __init__(self, name: str, sock: socket.socket):
        super().__init__(daemon=True)
        self.sock = sock
        self.name = name

    # clean up
    def _close(self):
        clients.remove(self.sock)
        self.sock.close()
        print(self.name + ' disconnected')

    def run(self):
        # read the length of filename 
        l_filename = int(self.sock.recv(4))
        # read the name of file
        data = self.sock.recv(l_filename)
        if data:
            filename = data.decode('utf-8')

            #check if file exists and add 'copyi_' to the begining of its name
            i = 0
            extra_part = ''
            while os.path.isfile(extra_part+filename):
                i += 1
                extra_part = 'copy'+str(i)+'_'
            filename = extra_part+filename
            f = open(filename, 'wb')
            print( self.name,'>','Receiving',filename,'...')
        else:
            # if we got no data – client has disconnected
            self._close()
            # finish the thread
            return
        while True:
            # try to read 1024 bytes from user
            # this is blocking call, thread will be paused here
            data = self.sock.recv(512)
            if data:
                f.write(data)
            else:
                # if we got no data – client has disconnected
                print(self.name,'>',filename,'was received.')
                f.close()
                self._close()
                # finish the thread
                return


def main():
    next_name = 1

    # AF_INET – IPv4, SOCK_STREAM – TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # reuse address; in OS address will be reserved after app closed for a while
    # so if we close and imidiatly start server again – we'll get error
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # listen to all interfaces at 8800 port
    sock.bind(('localhost', 8800))
    sock.listen()
    while True:
        # blocking call, waiting for new client to connect
        con, addr = sock.accept()
        clients.append(con)
        name = 'u' + str(next_name)
        next_name += 1
        print(str(addr) + ' connected as ' + name)
        # start new thread to deal with client
        ClientListener(name, con).start()


if __name__ == "__main__":
    main()
