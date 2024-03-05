"""
Two examples of how multiple private keys can be used.

Network: ZetaChain
Token: Zeta
"""

from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

private_keys = []

with open("private_keys.txt", "r") as f:
    for line in f:
        line = line.strip()
        private_keys.append(line)


node_url = "https://zetachain-mainnet-archive.allthatnode.com:8545"

"""
Example 1: Multiple Private keys & NO Proxies
Create private_keys.txt before launch
"""
def transact(private_key):
    value = 0  # value to send
    to_account = "RECEIVER_ADDRESS"  # change the receiver address
    web3 = Web3(HTTPProvider(node_url))
    from_account = web3.eth.account.from_key(private_key)

    nonce = web3.eth.get_transaction_count(from_account.address)
    tx = {
        "to": to_account,
        "value": value,
        "gas": 21000,
        "gasPrice": web3.eth.gas_price,
        "nonce": nonce,
        "chainId": 7000,
    }
    signed_tx = from_account.sign_transaction(tx)
    transaction_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        return f"Transaction {transaction_hash} failed!"

    return transaction_hash


if __name__ == "__main__":
    for private_key in private_keys:
        print(transact(private_key))


"""
Example 2:
The same example but with proxy usage. Create private_keys.txt and proxies.txt before launch.
Proxy format in file: login:password@ip:port (http only)
Keys and Proxy quantity must be equal.
"""

from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
from requests.sessions import Session

private_keys = []
proxies = []

with open("private_keys.txt", "r") as f:
    for line in f:
        line = line.strip()
        private_keys.append(line)

with open("proxies.txt", "r") as p:
    for proxy in p:
        proxy = proxy.strip()
        proxies.append(proxy)


node_url = "https://zetachain-mainnet-archive.allthatnode.com:8545"


def transact(private_key, proxy):
    # create proxies.txt file before launching!
    # proxy format in file: login:password@ip:port
    proxy_settings = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    session = Session()
    session.proxies = proxy_settings
    current_ip = session.get("https://api.ipify.org/")
    print(f"Using current IP: {current_ip.text}")

    custom_provider = HTTPProvider(node_url, session=session)
    web3 = Web3(custom_provider)
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    from_account = web3.eth.account.from_key(private_key)
    to_account = "RECEIVER_ADDRESS"  # change the receiver address
    value = 0  # value to send

    nonce = web3.eth.get_transaction_count(from_account.address)
    tx = {
        "from": from_account.address,
        "to": from_account.address,
        "value": value,
        "gas": 21000,
        "gasPrice": web3.eth.gas_price,
        "nonce": nonce,
        "chainId": 7000,
    }
    signed_tx = from_account.sign_transaction(tx)
    transaction_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()
    receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
    if receipt.status != 1:
        return f"Transaction {transaction_hash} failed!"

    return transaction_hash


if __name__ == "__main__":
    for i, private_key in enumerate(private_keys):
        proxy = proxies[i % len(proxies)]
        print(transact(private_key, proxy))
