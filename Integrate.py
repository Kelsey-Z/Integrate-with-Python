# deploy and interact with the Smart Contract
import json
import time
import pprint
from web3 import Web3

contract_address = [0x4C78920d3148cA05536F1D67A1F963B638657984]

#Because some features of Web3.py have not been fully audited to ensure security, we need to call w3.eth. Enable_unaudited_features() to confirm that we know that a problem might occur.
w3.eth.enable_unaudited_features()

# Connection to the local Ganache Blockchain
ganache_url = "HTTP://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
print(w3.isConnected())
print(w3.eth.blockNumber)

contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi)

# Owner is already set as the first one who deploy smart contract on Remix 
# address of the grid is also set by calling the constructor function 
# 1. Use owner account to register producer and consumer account

######## Here is the code I think very silly... To put them into the contract function, I need to put these information one by one #################
# The Producer:
Producer1_address = w3.eth.accounts[3] # Affect the producer to the 3rd account of the blockchain
Producer2_address = w3.eth.accounts[4]
Producer3_address = w3.eth.accounts[5]
# The Consumer:
Consumer1_address = w3.eth.accounts[6]
Consumer2_address = w3.eth.accounts[7]
Consumer3_address = w3.eth.accounts[8]
Consumer4_address = w3.eth.accounts[9]
Consumer5_address = w3.eth.accounts[10] 
#call function to register producer
tx_hash = contract.functions.registerProducer(Producer1_address, 'Producer1', 'Producer1@123.com', 'EH8').transact()
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
producerData = contract.functions.registerProducer(Producer1_address).call()
#call function to register consumer
tx_hash = contract.functions.registerConsumer(Consumer1_address, 'Consumer1', 'Consumer1@123.com', 'EH8').transact()
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
consumerData = contract.functions.registerConsumer1(Consumer1_address).call()
""" print("Transaction receipt mined: \n")
pprint.pprint(dict(receipt)) """

# 2.Use producer account to upload offer
print("Submitting Offer from producer\n")
tx_hash = contract.functions.uploadOffer(1, 15, 10).transact({'from': Producer1_address})
# the functions.transact() executes the specified function by sending a new public transaction.
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# arg(1) =1 is the offerID
# arg(2) =15 is the sellPricePerUnit
# arg(3) =10 is the totalUnits

# 3.Use consumer account to reserve offer
tx_hash = contract.functions.reserveOffer(Producer1_address, 11, 1, 15, 10).transact({'from': Consumer1_address})
receipt = w3.eth.waitForTransactionReceipt(tx_hash)
# arg(2) = 11 is _bidID
# arg(3) = 1 is offerID
# arg(4) = 15 is bidPricePerUnit
# arg(5) = 10 is bidUnits
"""   print("Transaction receipt mined: \n")
pprint.pprint(dict(receipt))
print("Was transaction successful? \n")
pprint.pprint(receipt['status']) """

# 4.Owner confirm order (including get the best bid)
########### I didn't finish the get best bid function in Python ###################
def getBestBid(_offerID): 

################### I didn't complete the following two functions because I didn't find ways to not input the data manually #############
# 5.Owner balance order (including upload smart meter data)

# 6.Owner complete order



