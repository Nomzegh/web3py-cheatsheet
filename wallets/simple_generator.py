from secrets import token_hex

from eth_account import Account


quantity = int(input('quantity: '))

private_keys = []
public_keys = []

for _ in range(quantity):

    private_key = '0x' + token_hex(32)
    public_key = Account.from_key(private_key).address

    private_keys.append(private_key)
    public_keys.append(public_key)

with open('private_keys.txt', mode='w') as file:
    file.write('\n'.join(private_keys))

with open('public_keys.txt', mode='w') as file:
    file.write('\n'.join(public_keys))
