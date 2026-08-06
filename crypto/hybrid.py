from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

from crypto.mlkem import encapsulate, decapsulate
from crypto.aes import (
    encrypt_file_with_key,
    decrypt_file_with_key,
)


def derive_aes_key(shared_secret):
    """
    Derive a 32-byte AES-256 key from the ML-KEM shared secret.
    """

    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"QuantumVault AES Key",
    )

    return hkdf.derive(shared_secret)


def encrypt_for_receiver(input_file,
                         encrypted_file,
                         receiver_public_key):

    ciphertext, shared_secret = encapsulate(receiver_public_key)

    aes_key = derive_aes_key(shared_secret)

    nonce = encrypt_file_with_key(
        input_file,
        encrypted_file,
        aes_key
    )

    return ciphertext, nonce


def decrypt_for_receiver(encrypted_file,
                         output_file,
                         receiver_private_key,
                         ciphertext,
                         nonce):

    shared_secret = decapsulate(
        receiver_private_key,
        ciphertext
    )

    aes_key = derive_aes_key(shared_secret)

    decrypt_file_with_key(
        encrypted_file,
        output_file,
        aes_key,
        nonce
    )