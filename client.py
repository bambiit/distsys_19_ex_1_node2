import socket
from random import randrange
from multiprocessing import Pool

HOST = '127.0.0.1'
PORT = 8002

def connectToServer(callNo):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        client_socket.send(str(randrange(100)))
        print "Connected to server ", callNo
        data = client_socket.recv(1024)
        print "Received from server: ", data
        client_socket.close()
        return
    except socket.error as err:
        print "Couldn't connect to server %s due to %s" % (callNo, err)

def Main():
    pool = Pool(processes=5)
    try:
        count = 5
        while count >= 1:
            callNo = 6 - count;
            pool.apply_async(connectToServer, (callNo,))
            count = count - 1
        pool.close()
        pool.join()
    except KeyboardInterrupt:
        pool.close()

if __name__ == '__main__':
    Main()
