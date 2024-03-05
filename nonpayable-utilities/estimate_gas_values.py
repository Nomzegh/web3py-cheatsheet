"""
This code estimates current gas values using connected RPC, and estimates the tx["gas"] using tx parameters
"""

from web3 import Web3


RPC_ENDPOINT = "https://zetachain-mainnet-archive.allthatnode.com:8545"

web3 = Web3(Web3.HTTPProvider(RPC_ENDPOINT))


def check_gas_fees():
    latest_block = web3.eth.get_block("latest")
    base_fee_per_gas = latest_block["baseFeePerGas"]

    base_fee_per_gas_gwei = web3.from_wei(base_fee_per_gas, "gwei")

    estimated_gas_price = web3.eth.gas_price
    estimated_gas_price_gwei = web3.from_wei(estimated_gas_price, "gwei")

    max_priority_fee_per_gas = web3.eth.max_priority_fee
    max_fee_per_gas = max_priority_fee_per_gas + base_fee_per_gas

    max_fee_per_gas_gwei = web3.from_wei(max_fee_per_gas, "gwei")
    max_priority_fee_per_gas_gwei = web3.from_wei(max_priority_fee_per_gas, "gwei")
    print(f"Legacy | Estimated Gas Price: {estimated_gas_price_gwei} gwei")
    print(f"EIP-1559 | Base Fee per Gas: {base_fee_per_gas_gwei} gwei")
    print(f"EIP-1559 | Max Priority Fee per Gas: {max_priority_fee_per_gas_gwei} gwei")
    print(f"EIP-1559 | Max Fee per Gas: {max_fee_per_gas_gwei} gwei\n")


def estimate_transaction_gas(tx):
    tx["gas"] = int(web3.eth.estimate_gas(tx) * 1.1)  # increase by 10% if needed

    return tx


if __name__ == "__main__":
    check_gas_fees()
    tx = {
        "from": "0x538E6eD28224D95d8278349FcaF937F9a717CfC9",
        "to": "0xcf1A40eFf1A4d4c56DC4042A1aE93013d13C3217",
        "value": web3.to_wei(0.00000001, "ether"),
        "nonce": web3.eth.get_transaction_count("0x538E6eD28224D95d8278349FcaF937F9a717CfC9"),
        "gasPrice": web3.eth.gas_price,
        "chainId": 7000,
        "data": "0xf340fa01000000000000000000000000538e6ed28224d95d8278349fcaf937f9a717cfc9",
    }
    print(estimate_transaction_gas(tx=tx))
    # {
    #   .......
    #   'gas': 61317
    # }
