import os

from crypto.mlkem import generate_keypair


KEY_FOLDER = "keys"

os.makedirs(KEY_FOLDER, exist_ok=True)


USERS = [

    "dhruv",

    "rahul",

    "eve"

]


for user in USERS:

    public_key, private_key = generate_keypair()

    with open(f"{KEY_FOLDER}/{user}_public.key", "wb") as f:
        f.write(public_key)

    with open(f"{KEY_FOLDER}/{user}_private.key", "wb") as f:
        f.write(private_key)

print("All ML-KEM Keys Generated Successfully!")