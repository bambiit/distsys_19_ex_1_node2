import threading
import time

print_lock = threading.Lock()
OK = 1
NOK = 0


class BankHandler:

    def __init__(self):
        pass

    def call_to_bank(self, amount):
        print_lock.acquire()
        print("Call to Bank")
        print_lock.release()
        time.sleep(5)

        try:
            amount = int(amount)
            if amount < 100:
                return NOK
            else:
                return OK
        except ValueError:
            return NOK
