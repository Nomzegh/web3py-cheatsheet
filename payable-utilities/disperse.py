"""
This code transfers an exact amount of native token from one address to multiple ones.
Create 'disperse_addresses.txt' file and paste all addresses for dispersing the native token
Network: BSC
Token: BNB
"""

from web3 import Web3


##################################
RPC = "https://rpc.ankr.com/rpc"
GAS_PRICE = 1.1
CHAIN_ID = 56
private_key = "YOUR_PRIVATE_KEY"
bnb_to_disperse = 0.0001 # on each wallet from disperse_addresses.txt
##################################

web3 = Web3(Web3.HTTPProvider(RPC))


def disperse(private_key: str, receiver: str, nonce: int) -> str:
    account = web3.eth.account.from_key(private_key)
    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(receiver),
        "value": web3.to_wei(bnb_to_disperse, "ether"),
        "nonce": nonce,
        "gasPrice": Web3.toWei(GAS_PRICE, "gwei"),
        "gas": 21000,
        "chainId": CHAIN_ID,
    }
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()

    return transaction_hash


if __name__ == "__main__":
    with open("disperse_addresses.txt", "r") as file:
        account = web3.eth.account.from_key(private_key)
        current_nonce = web3.eth.get_transaction_count(account.address)
        for address in file:
            address = address.strip()
            print(disperse(private_key, address, current_nonce))
            current_nonce += 1
