import threading
import time

print_lock = threading.Lock()

class BankHandler:

    def __init__(self):
        pass

    def call_to_bank(self, data):
        print_lock.acquire()
        print "Call to Bank"
        print_lock.release()
        time.sleep(10)
        try:
            amount = int(data)
            if amount < 100:
                return "NOT OK"
            else:
                return "OK"
        except ValueError:
            return "NOT OK"
