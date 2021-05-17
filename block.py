import hashlib
import time

class Block(object):
  # Initial structure of the block class:
  def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
    self.index = index
    self.proof_number = proof_number
    self.previous_hash = previous_hash
    self.data = data
    self.timestamp = timestamp or time.time()

    """ 
    The class constructor or initiation method (__init__) takes the following params:
     - self: param used to refer to the class itself. Any variable associated with the class can be accessed using it.
     - index: used to track the position of the block within the blockchain.
     - previous_hash: used to ref the hash of the previous block within the blockchain.
     - data: it gives details of the transactions done, for example, the amount bought.
     - timestamp: it inserts a timestamp for all the transactions performed.  
    """

  # Producing the cryptographic hash of each block:
  @property
  def compute_hash(self):
    string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)
    return hashlib.sha256(string_block.encode()).hexdigest()


    """
    The compute_hash class is used to produce the cryptographic hash of each block based on the above values.
    The SHA-256 algo was imported for use in getting the hashes of the blocks.
    Once the values have been placed inside the hashing module, the algo will return a 256-bit string labelling the contents of the block.
    THIS is what gives the blockchain immutability. Since each block will be represented by a hash, which will be computed from the hash of the previous block, corrupting any block in the chain will make the other blocks have invalid hashes, breaking the whole blockchain network.
    """