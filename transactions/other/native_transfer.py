from web3 import Web3


RPC = "HTTP://127.0.0.1:7545" # Ganache local RPC
web3 = Web3(Web3.HTTPProvider(RPC))


def transfer(private_key: str, receiver: str, value: float) -> str:
    account = web3.eth.account.from_key(private_key)
    tx = {
        "from": account.address,
        "to": web3.to_checksum_address(receiver),
        "value": web3.to_wei(value, "ether"),
        "nonce": web3.eth.get_transaction_count(account.address),
        "gasPrice": web3.eth.gas_price,
        "chainId": 1337,  # Change according to your network ID, 1 for Mainnet
    }
    tx["gas"] = int(web3.eth.estimate_gas(tx))
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        return f"Transaction {transaction_hash} failed!"

    return transaction_hash


if __name__ == "__main__":
    print(
        transfer(input("Private key: "), input("Receiver: "), float(input("Value: ")))
    )
