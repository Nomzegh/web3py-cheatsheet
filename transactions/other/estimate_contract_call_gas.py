"""
This code estimates the exact amount of gas needed for transaction to execute.
"""

from web3 import Web3

# Initialize web3 instance with your RPC URL
web3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/bsc"))

# Transaction object
tx = {
    "from": "0xcFc25f3f5a2543C1673C966a2d6F16b4ABff88d6",  # example user address
    "to": "0xEb6599AAaBb4A1E771bF5C6f58C509AA48805b57",  # example receiver (contract address in most cases)
    "data": "0xdfd378f9000000000000000000000000000000000000000000000a9698316fee6a800000",  # transaction data
}

estimated_gas = web3.eth.estimate_gas(tx)
print(f"Estimated Gas: {estimated_gas} wei")


"""
You can use the code below with own contract functions
"""
# Taken from https://github.com/Nomzegh/zetachain-automation/blob/main/functions.py
#
# def pool_tx(private_key: str, proxy=None):
#     web3 = create_web3_with_proxy(RPC, proxy)
#     contract = web3.eth.contract(
#         address=web3.to_checksum_address("0x2ca7d64A7EFE2D62A725E2B35Cf7230D6677FfEe"),
#         abi=pool_abi,
#     )
#     account = web3.eth.account.from_key(private_key)
#     tx = contract.functions.addLiquidityETH(
#         web3.to_checksum_address("0x48f80608B672DC30DC7e3dbBd0343c5F02C738Eb"),
#         web3.to_wei(bnb_value_zeta, "ether"),
#         0,
#         0,
#         account.address,
#         web3.eth.get_block("latest").timestamp + 3600,
#     ).build_transaction(
#         {
#             "from": account.address,
#             "value": web3.to_wei(pool_zeta_value, "ether"),
#             "nonce": web3.eth.get_transaction_count(account.address),
#             "gasPrice": web3.eth.gas_price,
#             "chainId": 7000,
#         }
#     )
#     tx["gas"] = int(web3.eth.estimate_gas(tx))
