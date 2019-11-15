import socket
from random import randrange
from multiprocessing import Pool

HOST = '127.0.0.1'
PORT = 8002



def connectToServer():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.send(str(randrange(100)))
    data = client_socket.recv(1024)
    print "Received from server: " + data
    client_socket.close()
    return

def Main():
    pool = Pool(processes=50)
    count = 50
    while count >= 1:
        pool.apply_async(connectToServer)
        count = count - 1
    pool.close()
    pool.join()

if __name__ == '__main__':
    Main()
