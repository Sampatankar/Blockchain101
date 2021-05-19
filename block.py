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
  THIS is what gives the blockchain immutability. Since each block will be represented by a hash, 
  which will be computed from the hash of the previous block, corrupting any block in the chain will make the other blocks have invalid hashes, 
  breaking the whole blockchain network.
"""

######################################################################################################

"""
The whole concept of a blockchain is based on the fact that the blocks are 'chained' to each other. 
In the code above the commentline we built a block, and in this module, we chain blocks together and manage the entire chain.
"""
class BlockChain(object):
  #Building the block chain:
  def __init__(self):
    self.chain = []
    self.current_data = []
    self.nodes = set()
    self.build_genesis()

    """
    The __init__ constructor method instantiates the blockchain using the following attributes:
     - self.chain: this variable stores all the blocks.
     - self.current_data: this variable stores information about the transactions in the block.
     - self.nodes: is a sample method for setting nodes.
     - self.build_genesis: this method is used to create the initial block in the chain.
    """

  #Creating the initial block:
  def build_genesis(self):
    self.build_block(proof_number=0, previous_hash=0)

  #Builds a new block and adds to the chain:
  def build_block(self, proof_number, previous_hash):
    block = Block(
      index = len(self.chain),
      proof_number = proof_number,
      previous_hash = previous_hash,
      data = self.current_data
    )

    self.current_data = []
    self.chain.append(block)

    return block

  """
  The build_genesis method is used to create the initial block in the chain, and as such the proof_number 
  and previous hash_figures are zero - sensible but arbitrary in this case.
  To initiate the creation of the chain, we call the build_block method and give it some default values, 
  and set the current data, then append the block to the chain.
  """


  #Checks whether the blockchain is valid:
  @staticmethod
  def confirm_validity(block, previous_block):
    if previous_block.index + 1 != block.index:
      return False

    elif previous_block.compute_hash() != block.previous_hash:
      return False

    elif block.timestamp <= previous_block.timestamp:
      return False

    return True
  
  """
  Confirming validity of the blockchain in critical in maintaining integrity of the chain.
  The series of if statements assesses whether the hash of each block has been compromised.
  It compares the hash values of every two successive blocks to identify anomalies:
     - If the chain is working correctly it returns True, and if not - False.
  """


  #Declares data of transactions:
  def get_data(self, sender, receiver, amount):
    self.current_data.append({
      'sender': sender,
      'receiver': receiver,
      'amount': amount,
    })

    return True

  """
  This simple method takes three parameters, and declares the data of the transactions on the block.
  The three parameters are added to the self.current_data list.
  """
  
  
  #Adds to the security of the blockchain:
  @staticmethod
  def proof_of_work(last_proof):
    pass

  """
  In blockchain tech, 'Proof of Work' (PoW) is a concept that refers to the complexity 
  involved in mining or generating new blocks on the blockchain.  
  E.g. PoW can be implemented by identifying a number that solves a problem whenever a user completes some computing work.
  Anyone on the blockchain should find the number difficult to identify, but easy to verify.
    - This is the main point behind PoW.
  This discourages spamming and compromising the integrity of the network - leading to a 'gas fee'.
  """


  #Returns the last block of the chain:
  @property
  def latest_block(self):
    return self.chain[-1]

  """
  This helper method is for retrieving the last block on the network, which is actually the current block.
  """

  
  #Implementation of blockchain mining:
  def block_mining(self, details_miner):
    self.get_data(
      sender="0", #this shows that THIS node has constructed another block
      receiver=details_miner,
      quantity=1, #creating a new block (or ID of the proof number) is awards 1 'unit'
    )

    last_block = self.latest_block
    last_proof_number = last_block.proof_number
    proof_number = self.proof_of_work(last_proof_number)
    last_hash = last_block.compute_hash

    block = self.build_block(proof_number, last_hash)

    return vars(block)

  """
  Initially, the transactions are kept in a list of unverified transactions.
  Mining refers to the process of placing the unverified transactions in a block
  and solving the PoW problem required.  This is what generates the work and the 
  'gas fee'.  
  If everything has been figured out correctly, a block is created or 'mined', 
  and 'chained' to the blockchain.  
  Mining blocks can sometimes elicit rewards of some kind for the use of their computing resources.
  """

  #####################################################################################################
  # FROM ORIGINAL D-ZONE ARTICLE - NOT IN MEDIUM ARTICLE:
  def create_node(self, address):
    self.nodes.add(address)
    return True

  @staticmethod
  def get_block_object(block_data):
    return Block(
      block_data['index'],
      block_data['proof_number'],
      block_data['previous_hash'],
      block_data['data'],
      timestamp=block_data['timestamp'],
    )



#######################################################################################################
# In both D-Zone & Medium article:
bc = BlockChain()
print("READY TO START MINING.")
print(bc.chain)

last_block = bc.latest_block
last_proof_number = last_block.proof_number
proof_number = bc.proof_of_work(last_proof_number)

bc.get_data(
  sender="0", #ID who created a new block
  receiver="Sam", #ME!!!
  amount=1, #Define the reward qty. for mining a block
)

last_hash = last_block.compute_hash
block = bc.build_block(proof_number, last_hash)
print("MINING SUCCESSFUL.")
print(bc.chain)