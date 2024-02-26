"""
This code automatically transfers all native balance using all private keys from private_keys.txt.
"""

from web3 import Web3


RPC = "HTTP://127.0.0.1:7545"
GAS_PRICE = 50
CHAIN_ID = 1337

web3 = Web3(Web3.HTTPProvider(RPC))


def transfer_all(private_key: str, receiver: str) -> str:
    account = web3.eth.account.from_key(private_key)
    balance = web3.eth.get_balance(account.address)
    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(receiver),
        "value": balance - (21000 * GAS_PRICE),
        "nonce": web3.eth.get_transaction_count(account.address),
        "gasPrice": Web3.toWei(GAS_PRICE, "gwei"),
        "gas": 21000,
        "chainId": CHAIN_ID,  # change according your network
    }
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    return (
        transaction_hash
        if receipt.status == 1
        else f"Transaction {transaction_hash} failed!"
    )


if __name__ == "__main__":
    receiver = input("Receiver address: ")
    with open("private_keys.txt", "r") as file:
        for private_key in file:
            private_key = private_key.strip()
            print(transfer_all(private_key, receiver))
