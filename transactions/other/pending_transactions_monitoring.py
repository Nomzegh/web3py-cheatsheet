import asyncio
import json
from web3 import Web3
from websockets import connect

# SET UP YOUR OWN NODE FOR THE BEST PERFORMANCE
ws_url = "wss://..." # websocket url
http_url = "https://..." # https url
web3 = Web3(Web3.HTTPProvider(http_url))


async def get_event():
    async with connect(ws_url) as ws:
        await ws.send(
            '{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}'
        )
        subscription_response = await ws.recv()
        print(subscription_response)

        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=15)
                response = json.loads(message)
                txHash = response["params"]["result"]
                print(txHash)
                pass
            except:
                pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(get_event())


# RESULT: Pending transaction hashes. Can be used with "web3.eth.get_transaction(hash)" and "tx_data_decode.py"
