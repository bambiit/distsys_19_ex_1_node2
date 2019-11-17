import socket
import thread
import threading
import bank

PORT = 8002
HOST = '127.0.0.1'
NOK = 0
OK = 1

print_lock = threading.Lock()


def threaded(connection, address):
    while True:
        amount = connection.recv(1024)
        if not amount:
            return return_to_client(NOK)
        result = bank.BankHandler().call_to_bank(amount)
        connection.send(return_to_client(result))
        print_lock.acquire()
        print("The payment server is sent data to ", address[0], ":", address[1])
        print_lock.release()
    connection.close()


def return_to_client(is_ok):
    if is_ok:
        return "OK"
    return "NOT OK"


def main():
    try:
        payment_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payment_socket.bind((HOST, PORT))
        payment_socket.listen(1)
        print("The payment server is listening")
        while True:
            (connection, address) = payment_socket.accept()
            print_lock.acquire()
            print("The payment server is connected to ", address[0], ":", address[1])
            print_lock.release()
            thread.start_new_thread(threaded, (connection, address))
        payment_socket.close()
    except KeyboardInterrupt:
        payment_socket.close()


if __name__ == '__main__':
    main()
