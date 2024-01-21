from web3 import Web3


RPC = "https://rpc.ankr.com/bsc"

web3 = Web3(Web3.HTTPProvider(RPC))
abi = """[
  {
    "constant": false,
    "inputs": [
      {
        "name": "_from",
        "type": "address"
      },
      {
        "name": "_to",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "transferFrom",
    "outputs": [
      {
        "name": "success",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
"""

contract = web3.eth.contract("0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56", abi=abi)


# contract: https://bscscan.com/token/0xe9e7cea3dedca5984780bafc599bd69add087d56#writeContract
# function: transferFrom(address sender, address recipient, uint256 amount)


def transfer_from(private_key: str, recipient: str, amount: float) -> str:
    account = web3.eth.account.from_key(private_key)
    tx = contract.functions.transferFrom(
        # function arguments:
        account.address,
        web3.to_checksum_address(recipient),  # recipient
        web3.to_wei(amount, "ether"),
    ).build_transaction(
        {
            "from": account.address,
            "value": 0,
            "nonce": web3.eth.get_transaction_count(account.address),
            "gasPrice": web3.eth.gas_price,
            "chainId": 56,  # BSC chainId
        }
    )
    tx["gas"] = int(web3.eth.estimate_gas(tx))
    signed_txn = web3.eth.account.sign_transaction(tx, private_key)
    transaction_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        return f"Transaction {transaction_hash} failed!"

    return f"Transfer hash: {transaction_hash}"


if __name__ == "__main__":
    print(
        transfer_from(
            input("Private key: "),
            input("Recipient address: "),
            float(input("Amount: ")),
        )
    )
