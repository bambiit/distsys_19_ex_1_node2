import socket
import thread
import threading
import bank

PORT = 8002
HOST = '127.0.0.1'
NOK = 0
OK = 1

print_lock = threading.Lock()


def threaded(connection, data, address):
    try:
        while True:
            bank_account, amount, name = data.decode('utf-8').split('\n')
            if not amount or not bank_account or not name:
                connection.close()
                return return_to_client(NOK)
            result = bank.BankHandler().call_to_bank(bank_account, int(amount), name)
            connection.send(return_to_client(result))
            print_lock.acquire()
            print("The payment server is sent data to ", address[0], ":", address[1])
            print_lock.release()
            connection.close()
    except Exception as err:
        print("There is an error ", err)
        connection.close()


def return_to_client(is_ok):
    if is_ok:
        return "OK"
    return "NOT ENOUGH MONEY IN THE BANK ACCOUNT"


def main():
    try:
        payment_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payment_socket.bind((HOST, PORT))
        payment_socket.listen(1024)
        print("The payment server is listening")
        while True:
            (connection, address) = payment_socket.accept()
            data = connection.recv(1024)
            if not data:
                connection.close()
                continue
            print_lock.acquire()
            print("The payment server is connected to ", address[0], ":", address[1])
            print_lock.release()
            thread.start_new_thread(threaded, (connection, data, address))
        payment_socket.close()
    except KeyboardInterrupt:
        payment_socket.close()


if __name__ == '__main__':
    main()
