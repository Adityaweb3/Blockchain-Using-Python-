from hashlib import sha256  #sha256 function will give us the ability to compute hashes
import json #We want JSON for parsing our data
import time  #time is used for timestamping.

class Chain:

    def __init__(self):

     self.blockchain = []    #blockchain is the actual list of our blocks

     self.pending = []  # pending is the list of transactions that are yet to be added.

     self.add_block(prevhash="Genesis", proof=123) 

    def add_transaction(self, sender, recipient, amount):

     transaction = {

        "sender": sender,

        "recipient": recipient,

        "amount": amount

    }

     self.pending.append(transaction)

    def compute_hash(self, block):

     json_block = json.dumps(block, sort_keys=True).encode()

     curhash = sha256(json_block).hexdigest()

     return curhash

    def add_block(self, proof, prevhash=None):

     block = {

        "index": len(self.blockchain),

        "timestamp": time.time(),

        "transactions": self.pending,

        "proof": proof,

        "prevhash": prevhash or self.compute_hash(self.blockchain[-1])

    }

     self.pending = []

     self.blockchain.append(block)

     chain = Chain()

t1 = chain.add_transaction("Aditya", "Abhishek", 100)

t2 = chain.add_transaction("Nitesh", "Vishal", 10)

t3 = chain.add_transaction("Sam", "Sree", 34)

chain.add_block(12345)

t4 = chain.add_transaction("Neeraj", "Harsh", 23)

t5 = chain.add_transaction("Dennis", "Brian", 3)

t6 = chain.add_transaction("Ken", "Doug", 88)

chain.add_block(6789)

print(chain.blockchain)



