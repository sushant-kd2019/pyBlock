# user class for the blockchain network
import json
import Transaction
from Utility import dump, hsh


class User:
    # initializing the variables
    def __init__(self, account_no, name, account_balance, password):
        self.account_no = account_no
        self.name = name
        self.account_balance = account_balance
        self.password = password

    # setter functions
    def set_name(self, current_password, new_name):
        if self.password == current_password:
            self.name = new_name
            return dump("1", "name has been reset")
        else:
            return dump("0", "current password is wrong")

    def set_password(self, current_password, new_password):
        if self.password == current_password:
            self.password = new_password
            return dump("1", "password has been reset")
        else:
            return dump("0", "current password is wrong")

    def update_balance(self, current_balance, change):
        if self.account_balance + change >= 0:
            self.account_balance += change
            return dump("1", "balance has been reset")
        else:
            return dump("0", "account balance is not enough")

    # getter functions
    def get_name(self):
        return self.name

    def get_balance(self):
        return self.account_balance

    # transaction functions

    def send_token(self, amount, reciever, message):
        tx = Transaction(amount, hsh(self.account_no), hsh(reciever), message)
        # I need to save these in a database

    def get_transactions(self):
        pass

    def create_contract(self):
        pass
