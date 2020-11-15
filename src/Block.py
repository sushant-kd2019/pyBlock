import Transaction
import json
from Utility import hsh, get_now

class Block:
    def __init__(self, prev_hash, tx_list):
        self.prev_hash = prev_hash
        self.tx_list = tx_list
        self.timestamp = get_now()
        self.block_hash = hsh((self.timestamp, tx_list))