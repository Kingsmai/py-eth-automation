import json
import random
import eth_account.signers.local
from web3 import Web3
import web3.contract.contract
import web3.types
import eth_account


with open('config.json', 'r') as f:
    config: dict = json.load(f)

# 用的测试网
rpc_list: list = config['SEPOLIA_RPC_LIST_HTTPS']
rpc: str = random.choice(rpc_list)
w3: Web3 = Web3(Web3.HTTPProvider(rpc))

if not w3.is_connected():
    print(f"Unable to connect to Web3 RPC: {rpc}")
    quit(1)

# Get current gas price:
gas_price: web3.types.Wei = w3.eth.gas_price
print(w3.from_wei(gas_price, "gwei"))

# 我的钱包地址
account_list: list = config['ACCOUNT_LIST_PRIVATE_KEY']
account: eth_account.signers.local.LocalAccount = w3.eth.account.from_key(
    account_list[0])

# 查询钱包余额
account_balance: web3.types.Wei = w3.eth.get_balance(account.address)
print(w3.from_wei(account_balance, "ether"))

# Load Contract ABI
# https://sepolia.etherscan.io/address/0x852138c55dc72558db2c8ded92e3c41b5bd1cb6d#readContract
contract_address = '0x852138C55Dc72558Db2c8deD92e3C41B5bD1cb6d'
with open(f'contract-abis/{contract_address}.abi.json', 'r') as f:
    contract_abi: dict = json.load(f)
    contract: web3.contract.contract.Contract = w3.eth.contract(
        contract_address, abi=contract_abi)

contract_name = contract.functions.getName().call()
print(contract_name)
