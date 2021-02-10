import Transaction

import json
from Utility import hsh, get_now,obj_dumps


class Block:
    def __init__(self, blockchain, prev_hash, proof, tx_list):
        self.block_no = blockchain.get_last_block_no()+1
        self.prev_hash = prev_hash
        self.tx_list = tx_list
        self.timestamp = get_now()
        self.proof = proof
        self.block_hash = hsh(obj_dumps(self))
        
