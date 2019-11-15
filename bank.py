class BankHandler:

    def __init__(self):
        pass

    def call_to_bank(self, data):
        try:
            amount = int(data)
            if amount < 100:
                return "NOT OK"
            else:
                return "OK"
        except ValueError:
            return "NOT OK"
