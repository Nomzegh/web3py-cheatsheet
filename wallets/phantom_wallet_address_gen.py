from solders.keypair import Keypair

# pip install solana
# generates private keys and addresses to keys.txt & addresses.txt

def generate_keys(qty):
    with open("keys.txt", "a") as keys_file, open(
        "addresses.txt", "a"
    ) as addresses_file:
        for i in range(qty):
            keypair = Keypair()
            address = keypair.pubkey()
            keys_file.write(str(keypair) + "\n")
            addresses_file.write(str(address) + "\n")

    print(f"Generated {qty} private keys & addresses")


generate_keys(int(input("Generate keys&addresses: ")))
