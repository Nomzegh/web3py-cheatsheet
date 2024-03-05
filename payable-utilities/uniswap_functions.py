"""
This file shows the usage of popular functions on Uniswap.
Network: Binance Smart Chain
Contracts: BNB (native), USDT
"""

from uniswap import Uniswap # pip install uniswap-python
from web3 import Web3


provider = "https://rpc.ankr.com/bsc"
private_key = None  # specify the private key for swap functions
address = None  # specify the address for swap functions

web3 = Web3()
uniswap = Uniswap(
    version=2, provider=provider, address=address, private_key=private_key
)

bnb = Web3.to_checksum_address(
    "0x0000000000000000000000000000000000000000"
)  # bnb contract address
usdt = Web3.to_checksum_address(
    "0x55d398326f99059ff775485246999027b3197955"
)  # usdt contract address


def estimate_price_input():
    # Returns the amount of USDT you get for 1 BNB
    bnb_amount = 1
    return web3.from_wei(
        uniswap.get_price_input(bnb, usdt, bnb_amount * 10**18), "ether"
    )


def estimate_price_output():
    # Returns the amount of BNB you need to pay to get 100 USDT
    usdt_desired_amount = 100
    return web3.from_wei(
        uniswap.get_price_output(bnb, usdt, usdt_desired_amount * 10**18), "ether"
    )


def swap_bnb_to_usdt():
    # Make a trade by specifying the quantity of the input token you wish to sell
    # Swaps (sells) the desired amount of BNB to USDT
    bnb_desired_amount = 1
    uniswap.make_trade(bnb, usdt, bnb_desired_amount * 10**18)  # sell 1 BNB for USDT


def swap_usdt_to_bnb():
    # Make a trade by specifying the quantity of the output token you wish to buy
    # Swaps (buys) the desired amount of USDT to BNB
    usdt_to_spend = 100
    uniswap.make_trade_output(bnb, usdt, usdt_to_spend * 10**18)  # buy BNB for 100 USDT
