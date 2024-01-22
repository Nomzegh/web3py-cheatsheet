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
        "name": "_tokenId",
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

contract = web3.eth.contract("0xE3b1D32e43Ce8d658368e2CBFF95D57Ef39Be8a6", abi=abi)


# contract: https://bscscan.com/address/0xe3b1d32e43ce8d658368e2cbff95d57ef39be8a6
# function: transferFrom(address from, address to, uint256 tokenId)


def transfer_from(private_key: str, recipient: str, token_id: float) -> str:
    account = web3.eth.account.from_key(private_key)
    tx = contract.functions.transferFrom(
        # function arguments:
        account.address,
        web3.to_checksum_address(recipient),  # recipient
        token_id,
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
            int(input("Token id: ")),
        )
    )
