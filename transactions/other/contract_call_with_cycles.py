from web3 import Web3
from bridge_abi import mantle_abi  # abi is imported from created file bridge_abi.py (link below)


MANTLE_RPC = "https://rpc.mantle.xyz"

web3 = Web3(Web3.HTTPProvider(MANTLE_RPC))
abi = mantle_abi
contract = web3.eth.contract("0x4200000000000000000000000000000000000010", abi=abi)


# contract: https://explorer.mantle.xyz/address/0x4200000000000000000000000000000000000010
# function: withdraw(address _l2Token, uint256 _amount, uint32 _l1Gas, bytes _data)

def withdraw(private_key: str, cycles: int) -> str:
    for i in range(int(cycles)):
        account = web3.eth.account.from_key(private_key)
        tx = contract.functions.withdraw(
            # function arguments:
            web3.to_checksum_address("0xdeaddeaddeaddeaddeaddeaddeaddeaddead0000"),  # 1
            10000000000000000,  # 2
            0,  # 3
            b"", # 4
        ).build_transaction(
            {
                "from": account.address,
                "value": 0,
                "nonce": web3.eth.get_transaction_count(account.address),
                "gasPrice": web3.eth.gas_price,
                "chainId": 5000,  # mantle chainId
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
    print(withdraw(input("Private key: "), input("Cycles: ")))
