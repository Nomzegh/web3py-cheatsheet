"""
This code decodes the tx["data"] and returns readable transaction inputs
You can also decode txData on https://openchain.xyz/tools/abi
"""

from web3 import Web3


##################################################################
abi = """YOUR_FUNCTION_ABI"""
contract_address = "YOUR_CONTRACT_ADDRESS"
RPC = "YOUR_RPC"
tx_hash = "TRANSACTION_HASH"
##################################################################


web3 = Web3(Web3.HTTPProvider(RPC))
contract = web3.eth.contract(
    address=web3.to_checksum_address(contract_address),
    abi=abi,
)


def decode_tx(tx_hash: str) -> str:
    tx = web3.eth.get_transaction(tx_hash)
    result = contract.decode_function_input(tx["input"])

    return result


if __name__ == "__main__":
    transaction_inputs = decode_tx(tx_hash)
    print(transaction_inputs)
