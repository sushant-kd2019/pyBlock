from Transaction import Transaction
from flask import Flask, request
from Blockchain import Blockchain
from Utility import obj_dumps, confirm_data, dump
from flask.json import jsonify
from uuid import uuid4


# creating an API for blockchain.
app = Flask(__name__)

node_id = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.blockchain[-1]
    last_proof, last_block_no = last_block.proof, last_block.block_no
    proof = blockchain.calculate_proof()
    if Blockchain.validate_pow(last_proof, proof):
        blockchain.add_block(proof)
        return dump("1", "block number: "+str(last_block_no))
    else:
        return dump('0', "mining failed")


@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    ar = request.get_json()
    if confirm_data(ar):
        response = blockchain.add_transaction(
            ar['amount'], ar['sender'], ar['reciever'], ar['message'])
    else:
        response = dump("0", "Transaction incomplete. Check your input.")
    return jsonify(response)


@app.route('/chain', methods=['GET'])
def get_blockchain():
    response = {
        'chain': obj_dumps(blockchain.blockchain),
        'length': blockchain.get_last_block_no()
    }
    return response

@app.route('/inc_diff',methods=['GET'])
def increase_difficulty():
    response = Blockchain.increase_difficulty()
    return response

@app.route('/dec_diff',methods=['GET'])
def decrease_difficulty():
    response = Blockchain.decrease_difficulty()
    return response

@app.route('/node/register', methods=['POST'])
def register_node():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return dump('0','list of nodes is invalid')
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'code':'1',
        'message':'nodes added successfully',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response)

@app.route('/node/resolve', methods = ['GET'])
def consensus():
    replaced = blockchain.consensus()
    if replaced:
        response = {
            'message' : 'Chain has been replaced',
            'chain' : blockchain.blockchain
        }
    else:
        response = {
            'message' : 'Chain is already authoritative',
            'chain' : blockchain.blockchain
        }
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


# ----------------------------------------------------------------------
