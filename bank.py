import time

class BankHandler:

    def __init__(self):
        pass

    def call_to_bank(self, data):
        print "Call to Bank"
        time.sleep(10)
        print "Return from Bank"
        try:
            amount = int(data)
            if amount < 100:
                return "NOT OK"
            else:
                return "OK"
        except ValueError:
            return "NOT OK"
