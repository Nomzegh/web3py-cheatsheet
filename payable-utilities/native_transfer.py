"""
This code is a simple transfer of native token.
Network: Binance Smart Chain
Token: BNB
"""

from web3 import Web3

##################################
RPC = "https://rpc.ankr.com/rpc"
CHAIN_ID = 56
GAS_PRICE = 1.1
value = 0.0001
receiver = "0x_receiver_address"
private_key = "YOUR_PRIVATE_KEY"
##################################

web3 = Web3(Web3.HTTPProvider(RPC))


def transfer(private_key: str, receiver: str, value: float) -> str:
    account = web3.eth.account.from_key(private_key)
    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(receiver),
        "value": web3.to_wei(value, "ether"),
        "nonce": web3.eth.get_transaction_count(account.address),
        "gasPrice": web3.to_wei(GAS_PRICE),
        "chainId": CHAIN_ID,
        "gas": 21000,
    }
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        return f"Transaction {transaction_hash} failed!"

    return transaction_hash


if __name__ == "__main__":
    print(transfer(private_key=private_key, receiver=receiver, value=value))
