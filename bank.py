import threading
import time

print_lock = threading.Lock()
OK = 1
NOK = 0


class BankHandler:

    def __init__(self):
        pass

    def call_to_bank(self, bank_account, amount, name):
        print_lock.acquire()
        print("Call to Bank")
        print_lock.release()
        time.sleep(5)

        if not bank_account or not name or not amount:
            return NOK

        # simulate call to Bank, return if NOK the amount < 100
        try:
            amount = int(amount)
            if amount < 100:
                return NOK
            else:
                return OK
        except ValueError:
            return NOK
