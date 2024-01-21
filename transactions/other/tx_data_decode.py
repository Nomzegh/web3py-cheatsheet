from web3 import Web3


abi = """PASTE_ABI_HERE_OR_IMPORT_FROM_FILE"""
contract_address = "0x123..."  # paste contract address here
RPC = "https://rpc.scroll.io"  # example RPC

web3 = Web3(Web3.HTTPProvider(RPC))
contract = web3.eth.contract(
    address=web3.to_checksum_address(contract_address),
    abi=abi,
)


def decode_tx(tx_hash: str) -> str:
    tx = web3.eth.get_transaction(tx_hash)
    result = contract.decode_function_input(tx["input"])

    return result
