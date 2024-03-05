"""
This code allows to use web3 with proxy.
It injects a connection layer to your Web3 HTTPProvider using requests.session with proxy
"""

from web3 import Web3
from requests.sessions import Session
from web3.middleware import geth_poa_middleware
from web3.providers.rpc import HTTPProvider


proxy = "http://login:password@ip:port"
node_url = "https://rpc.ankr.com/eth"

proxy_settings = {
    "http": proxy,
    "https": proxy,
}

session = Session()
session.proxies = proxy_settings

# you may check if proxy works
# proxy_ip = session.get("https://api.ipify.org").text
# print(proxy_ip)

custom_provider = HTTPProvider(node_url, session=session)
w3 = Web3(custom_provider)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(w3.is_connected()) # is connected: True/False
