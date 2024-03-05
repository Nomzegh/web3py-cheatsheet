"""
This code is an example of EIP-1559 transaction (simple native token transfer).
Network: ZetaChain
Token: ZETA
"""

from web3 import Web3

##################################
RPC = "https://zetachain-mainnet-archive.allthatnode.com:8545"
CHAIN_ID = 7000
private_key = "YOUR_PRIVATE_KEY"
receiver = "0x_receiver_address"
value = 0.0001 # ZETA token
##################################

web3 = Web3(Web3.HTTPProvider(RPC))


def transfer(private_key: str, receiver: str, value: float) -> str:
    account = web3.eth.account.from_key(private_key)
    base_fee = web3.eth.get_block("latest")["baseFeePerGas"]
    max_priority_fee = web3.eth.max_priority_fee
    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(receiver),
        "value": web3.to_wei(value, "ether"),
        "nonce": web3.eth.get_transaction_count(account.address),
        "maxFeePerGas": base_fee + max_priority_fee,
        "maxPriorityFeePerGas": max_priority_fee,
        "chainId": CHAIN_ID,
        "gas": 21000,
    }
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        return f"Transaction {transaction_hash} failed!"

    return transaction_hash


print(transfer(private_key=private_key, receiver=receiver, value=value))
