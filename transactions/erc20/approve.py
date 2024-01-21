from web3 import Web3
from contracts_abi import (
    erc20_abi,
)  # import your own abi variable of whatever erc20 contract


MANTLE_RPC = "YOUR_RPC"

web3 = Web3(Web3.HTTPProvider(MANTLE_RPC))
abi = erc20_abi
amount = 10  # amount of ERC20 token to be approved
contract = "0xabcdef..."  # whatever ERC20 contract address


contract = web3.eth.contract(contract, abi=abi)


def approve(private_key: str, cycles: int) -> str:
    for i in range(int(cycles)):
        account = web3.eth.account.from_key(private_key)
        tx = contract.functions.approve(
            # function arguments:
            web3.to_checksum_address(
                "0xabcdef..."
            ),  # spender address (in most cases, DEX router address)
            web3.to_wei(amount),  # if 18 decimals ! ! !
        ).build_transaction(
            {
                "from": account.address,
                "value": 0,
                "nonce": web3.eth.get_transaction_count(account.address),
                "gasPrice": web3.eth.gas_price,
                "chainId": 1337,  # change chainId
            }
        )
        tx["gas"] = int(web3.eth.estimate_gas(tx))
        signed_txn = web3.eth.account.sign_transaction(tx, private_key)
        transaction_hash = web3.eth.send_raw_transaction(
            signed_txn.rawTransaction
        ).hex()
        receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
        if receipt.status != 1:
            return f"Transaction {transaction_hash} failed!"

        return f"Bridge hash: {transaction_hash}"


if __name__ == "__main__":
    print(approve(input("Private key: "), input("Cycles: ")))
