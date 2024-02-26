from web3 import Web3


RPC_ENDPOINT = "https://rpc.ankr.com/bsc" # Binance Smart Chain RPC
web3 = Web3(Web3.HTTPProvider(RPC_ENDPOINT))


def check_current_gas_price():
    current_gas_price = web3.eth.gas_price
    current_gas_price_gwei = web3.from_wei(current_gas_price, "gwei")
    print(f"Current gas price: {current_gas_price_gwei} gwei")


if __name__ == "__main__":
    check_current_gas_price()
