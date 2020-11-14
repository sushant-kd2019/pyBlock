#transaction
from Utility import get_now,hsh

class Transaction:
    tx_no=1

    def __init__(self, amount, hash_sender, hash_reciever, message=None):
        self.amount = amount
        self.hash_sender = hash_sender
        self.hash_reciever = hash_reciever
        self.message = message
        self.timestamp = get_now()
        self.txhash = hsh(tuple(self.amount, self.hash_sender, self.hash_reciever, self.message, self.timestamp))

