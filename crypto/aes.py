import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_aes_key():
    """
    Generates a random 256-bit AES key.
    """
    return AESGCM.generate_key(bit_length=256)


def encrypt_file(input_path, output_path):
    """
    Encrypts a file using AES-256-GCM.

    Returns:
        key, nonce
    """

    # Generate AES key
    key = generate_aes_key()

    # AES-GCM object
    aes = AESGCM(key)

    # Random 12-byte nonce
    nonce = os.urandom(12)

    # Read original file
    with open(input_path, "rb") as file:
        data = file.read()

    # Encrypt
    encrypted_data = aes.encrypt(nonce, data, None)

    # Save encrypted file
    with open(output_path, "wb") as file:
        file.write(encrypted_data)

    return key, nonce


def decrypt_file(input_path, output_path, key, nonce):
    """
    Decrypts AES-256 encrypted file.
    """

    aes = AESGCM(key)

    with open(input_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = aes.decrypt(
        nonce,
        encrypted_data,
        None
    )

    with open(output_path, "wb") as file:
        file.write(decrypted_data)

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_file_with_key(input_path, output_path, key):
    """
    Encrypt a file using the provided 32-byte AES key.
    Returns the nonce used for AES-GCM.
    """

    aes = AESGCM(key)

    nonce = os.urandom(12)

    with open(input_path, "rb") as file:
        data = file.read()

    encrypted_data = aes.encrypt(nonce, data, None)

    with open(output_path, "wb") as file:
        file.write(encrypted_data)

    return nonce


def decrypt_file_with_key(input_path, output_path, key, nonce):
    """
    Decrypt a file using the provided AES key.
    """

    aes = AESGCM(key)

    with open(input_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = aes.decrypt(nonce, encrypted_data, None)

    with open(output_path, "wb") as file:
        file.write(decrypted_data)