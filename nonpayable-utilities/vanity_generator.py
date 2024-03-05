"""
This code generates an address with desired prefix (vanity address)
"""

from eth_keys import keys
from secrets import token_bytes


desired_prefix = "da7baeb"


def generate_vanity_address(prefix):
    prefix = prefix.lower()
    count = 0
    while True:
        count += 1
        print(count)
        private_key_bytes = token_bytes(32)
        private_key = keys.PrivateKey(private_key_bytes)
        public_key = private_key.public_key
        address = public_key.to_checksum_address()

        if address.lower().startswith(f"0x{prefix}"):
            return address, private_key


address, private_key = generate_vanity_address(desired_prefix)
print(f"Vanity Address: {address}")
print(f"Private Key: {private_key}")


# version with multiprocessing written by chatgpt

# from eth_keys import keys
# from secrets import token_bytes
# import multiprocessing
# from queue import Empty

# desired_prefix = "dead"
# number_of_processes = 5


# def generate_vanity_address(queue, prefix):
#     prefix = prefix.lower()
#     while True:
#         private_key_bytes = token_bytes(32)
#         private_key = keys.PrivateKey(private_key_bytes)
#         public_key = private_key.public_key
#         address = public_key.to_checksum_address()

#         if address.lower().startswith(f"0x{prefix}"):
#             queue.put((address, private_key))
#             return


# def listener(queue):
#     while True:
#         try:
#             address, private_key = queue.get(timeout=1)
#             print(f"Vanity Address: {address}")
#             print(f"Private Key: {private_key}")
#             break
#         except Empty:
#             continue


# if __name__ == "__main__":
#     manager = multiprocessing.Manager()
#     queue = manager.Queue()

#     listener_process = multiprocessing.Process(target=listener, args=(queue,))
#     listener_process.start()

#     processes = []
#     for _ in range(number_of_processes):
#         p = multiprocessing.Process(
#             target=generate_vanity_address, args=(queue, desired_prefix)
#         )
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

#     listener_process.terminate()
#     listener_process.join()
