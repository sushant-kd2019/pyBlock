# transaction
import json
from Utility import get_now, hsh


class Transaction:
    tx_no = 0
    @staticmethod
    def tx_index():
        Transaction.tx_no += 1
        return Transaction.tx_no


    def __init__(self, amount, sender, reciever, message=None):
        self.index = Transaction.tx_index()
        self.amount = amount
        self.sender = sender
        self.reciever = reciever
        self.message = message
        self.timestamp = get_now()
        self.txhash = hsh(json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=True, indent=4))

