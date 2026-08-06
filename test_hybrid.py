from crypto.hybrid import encrypt_for_receiver, decrypt_for_receiver
from utils.key_loader import load_public_key, load_private_key

# Load Rahul's keys
rahul_public = load_public_key("rahul")
rahul_private = load_private_key("rahul")

# Encrypt
ciphertext, nonce = encrypt_for_receiver(
    "uploads/sample.txt",
    "encrypted/sample.enc",
    rahul_public
)

print("✅ File encrypted successfully!")

# Decrypt
decrypt_for_receiver(
    "encrypted/sample.enc",
    "decrypted/sample.txt",
    rahul_private,
    ciphertext,
    nonce
)

print("✅ File decrypted successfully!")