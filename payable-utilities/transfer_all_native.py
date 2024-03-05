"""
This code transfers all native balance using all private keys from private_keys.txt.
Create private_keys.txt and paste the private keys you want to transfer all native balance from.
Network: BSC
"""

from web3 import Web3

##################################
RPC = "https://rpc.ankr.com/rpc"
GAS_PRICE = 1.1
CHAIN_ID = 56
receiver_address = "0x_receiver_address"
##################################

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
        "chainId": CHAIN_ID,
    }
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

    return transaction_hash


if __name__ == "__main__":
    with open("private_keys.txt", "r") as file:
        for private_key in file:
            try:
                private_key = private_key.strip()
                print(transfer_all(private_key, receiver_address))
            except Exception as e:
                print(e)
