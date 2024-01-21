from web3 import Web3


balanceOf_abi = """[
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "balance",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
]
"""

MANTLE_RPC = "https://rpc.ankr.com/bsc"

web3 = Web3(Web3.HTTPProvider(MANTLE_RPC))
abi = balanceOf_abi
contract = web3.to_checksum_address(
    "0xe9e7cea3dedca5984780bafc599bd69add087d56"
)  # whatever ERC20 contract address


contract = web3.eth.contract(contract, abi=abi)


# contract: https://bscscan.com/token/0xe9e7cea3dedca5984780bafc599bd69add087d56#readContract
# function: balanceOf(address account) -> ERC20 balance of address in wei


def balance(address) -> str:
    address = web3.to_checksum_address(address)
    result = contract.functions.balanceOf(
        # function arguments:
        web3.to_checksum_address(address),  # address
    ).call()

    return f"Balance of {address}: {web3.from_wei(result, 'ether')}"


if __name__ == "__main__":
    print(balance(input("Address: ")))

# Address: 0x557E074A059D0c9d0762631018668D06351C2787 #random address from bscscan
# Balance of 0x557E074A059D0c9d0762631018668D06351C2787: 42.343735200920151115
