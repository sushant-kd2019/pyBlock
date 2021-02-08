from Block import Block
from Transaction import Transaction
from Utility import dump, hsh
# ----------------------------------------------------------------------


class Blockchain(object):
    def __init__(self):
        self.blockchain = []
        self.transaction_queue = []

        # initiate the first block.
        b = Block(self,prev_hash=1, proof=100, tx_list=[])
        self.blockchain.append(b)

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

    def consensus(self):
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
        return trial_hash[Blockchain.difficulty*(-1):] == "0"*Blockchain.difficulty

# ----------------------------------------------------------------------
