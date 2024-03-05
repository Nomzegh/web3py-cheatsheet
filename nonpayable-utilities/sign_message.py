"""
This code signs a message with private key and returns a signature
"""

from web3 import Web3
from eth_account.messages import encode_defunct


web3 = Web3()

message_to_sign = "Sign this message to sign in!"
private_key = "YOUR_PRIVATE_KEY"


def sign_with_key(private_key, message):
    account = web3.eth.account.from_key(private_key)
    signature = account.sign_message(encode_defunct(text=message)).signature.hex()

    return signature


if __name__ == "__main__":
    signature = sign_with_key(private_key=private_key, message=message_to_sign)
    print(signature)
    # 0x0551efc9be58debc8f82d7b.........


# Example from https://github.com/Nomzegh/zetachain-automation/blob/main/functions.py
#
# def generate_signature(private_key: str, proxy=None) -> hex:
#     web3 = create_web3_with_proxy(RPC, proxy)
#     msg = {
#         "types": {
#             "Message": [{"name": "content", "type": "string"}],
#             "EIP712Domain": [
#                 {"name": "name", "type": "string"},
#                 {"name": "version", "type": "string"},
#                 {"name": "chainId", "type": "uint256"},
#             ],
#         },
#         "domain": {"name": "Hub/XP", "version": "1", "chainId": 7000},
#         "primaryType": "Message",
#         "message": {"content": "Claim XP"},
#     }

#     encoded_data = encode_structured_data(msg)
#     result = web3.eth.account.sign_message(encoded_data, private_key)
#     claim_signature = result.signature.hex()

#     return claim_signature
