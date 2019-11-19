import socket
from random import randrange
from multiprocessing import Pool
from contextlib import closing

HOST = ''
PORT = 8002


def connect_to_payment_server(call_no):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.settimeout(10)
        client_socket.connect((HOST, PORT))
        # client_socket.send(str(randrange(200)))
        bank_account = randrange(1000000000000000000000000, 2000000000000000000000000)
        amount = randrange(200)
        name = "AAAAABBBBBCCCCC"
        client_socket.sendall(str.encode("\n".join([str(bank_account), str(amount), name])))
        print("Connected to server ", call_no)
        data = client_socket.recv(1024)
        print "Received from server: ", data
        client_socket.close()
    except socket.error as err:
        print("Couldn't connect to server %s due to %s" % (call_no, err))
        client_socket.close()


def main():
    loop = 5
    call_no_array = []
    for x in range(0, loop):
        call_no_array.append(x)

    with closing(Pool(processes=5)) as pool :
        pool.map(connect_to_payment_server, call_no_array)
        pool.terminate()


if __name__ == '__main__':
    main()
