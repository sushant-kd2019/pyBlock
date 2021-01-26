import Transaction
from Blockchain import Blockchain
import json
from Utility import hsh, get_now


class Block:
    def __init__(self, prev_hash, proof, tx_list):
        self.block_no = Blockchain.get_last_block_no()+1
        self.prev_hash = prev_hash
        self.tx_list = tx_list
        self.timestamp = get_now()
        self.block_hash = hsh(json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=True, indent=4))
        self.proof = proof
