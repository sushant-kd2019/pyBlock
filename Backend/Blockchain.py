from Block import Block
from Transaction import Transaction
from Utility import dump, hsh
from urllib.parse import urlparse
import requests
# ----------------------------------------------------------------------


class Blockchain(object):
    def __init__(self):
        self.blockchain = []
        self.transaction_queue = []
        self.node_list = set()

        # initiate the first block.
        b = Block(self,prev_hash=1, proof=100, tx_list=[])
        self.blockchain.append(b)

    def add_node(self,address):
        url = urlparse(address)
        self.node_list.add(url.netloc())

    def validate_chain(self, chain):
        last_block = chain[0]
        for i in range(1,len(chain)):
            b = chain[i]
            if b['prev_hash'] != hsh[last_block]:
                return False
            if not Blockchain.validate_pow(last_block['proof'],b['proof']):
                return False
            last_block = chain[i]
        return True
    
    def consensus(self):
        neighbour_nodes = self.node_list
        new_chain = None
        length = len(self.blockchain)
        for node in neighbour_nodes:
            response = requests.get(f'http://{node}/chain')
            if response.status_code == 200:
                l = response.json()['length']
                chain = response.json()['chain']

                if l>length and self.validate_chain(chain):
                    length = l
                    new_chain = chain
            if new_chain:
                self.blockchain = new_chain
                return True
            return False
        


    def add_block(self, proof):
        last_block = self.blockchain[-1]
        b = Block(self,prev_hash=last_block.block_hash,
                  proof=proof, tx_list=self.transaction_queue)
        self.blockchain.append(b)
        return dump("1", "Block created and added to blockchain.")

    def add_transaction(self, amount, sender, reciever, msg):
        tx = Transaction(amount, sender, reciever, msg)
        self.transaction_queue.append(tx)
        return dump("1", "Transaction complete.")

    def calculate_proof(self):
        proof = 0
        last_proof = self.get_last_block().proof
        while not Blockchain.validate_pow(last_proof, proof):
            proof += 1
        return proof

    def get_last_block(self):
        return self.blockchain[-1]

    def get_last_block_no(self):
        return len(self.blockchain)

    # ----------------------------------------------------------------------
    difficulty = 3

    @staticmethod
    def increase_difficulty():
        Blockchain.difficulty += 1
        return dump('1',"difficulty increased by 1. New difficulty: "+str(Blockchain.difficulty))

    @staticmethod
    def decrease_difficulty():
        if Blockchain.difficulty>=2:
            Blockchain.difficulty -= 1
            return dump('1',"difficulty decreased by 1. New difficulty: "+str(Blockchain.difficulty))
        else:
            return dump('0','Not possible to decrease difficulty. Lower limit reached.')
    
    @staticmethod
    def validate_pow(last_proof, proof):
        trial_hash = hsh("%d%d" % (proof, last_proof))
        return bool(trial_hash[Blockchain.difficulty*(-1):] == "0"*Blockchain.difficulty)

# ----------------------------------------------------------------------
