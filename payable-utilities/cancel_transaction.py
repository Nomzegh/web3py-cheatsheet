"""
This code cancels your previous transaction which is stuck for some reason (f.e low gasPrice)
You have to set a higher gasPrice than in your stuck transaction
Network: Binance Smart Chain
"""

from web3 import Web3


##################################
RPC = "https://rpc.ankr.com/rpc"
CHAIN_ID = 56
gas_price = 3  # set higher gasprice than in your stuck TX
private_key = "YOUR_PRIVATE_KEY"
##################################

web3 = Web3(Web3.HTTPProvider(RPC))


def cancel_transaction(private_key: str) -> str:
    account = web3.eth.account.from_key(private_key)
    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(account.address),
        "value": 0,
        "nonce": web3.eth.get_transaction_count(account.address, "pending") - 1,
        "gasPrice": web3.to_wei(gas_price),
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
    print(cancel_transaction())
