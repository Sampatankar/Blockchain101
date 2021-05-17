"""
The whole concept of a blockchain is based on the fact that the blocks are 'chained' to each other. 
In block.py we built a block, and in this module, we chain blocks together and manage the entire chain.
"""
class BlockChain(object):
  #Building the block chain:
  def __init__(self):
    self.chain = []
    self.current_data = []
    self.nodes = set()
    self.build.genesis()

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
    The build_genesis method is used to create the initial block in the chain, and as such the proof_number and previous hash_figures are zero - sensible but arbitrary in this case.
    To initiate the creation of the chain, we call the build_block method and give it some default values, and set the current data, then append the block to the chain.
    """

  @staticmethod
  #Checks whether the blockchain is valid:
  def confirm_validity(block, previous_block):
    pass

  #Declares data of transactions:
  def get_data(self, sender, receiver, amount):
    pass

  @staticmethod
  #Adds to the security of the blockchain:
  def proof_of_work(last_proof):
    pass

  @property
  #Returns the last block of the chain:
  def latest_proof(self):
    pass