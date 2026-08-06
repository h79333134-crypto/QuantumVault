from pqcrypto.kem import ml_kem_768


def generate_keypair():
    """
    Generate ML-KEM-768 key pair.
    Returns:
        public_key, private_key
    """
    public_key, private_key = ml_kem_768.generate_keypair()
    return public_key, private_key


def encapsulate(public_key):
    """
    Encrypt (encapsulate) a shared secret
    using the receiver's public key.

    Returns:
        ciphertext, shared_secret
    """
    ciphertext, shared_secret = ml_kem_768.encrypt(public_key)
    return ciphertext, shared_secret


def decapsulate(private_key, ciphertext):
    """
    Recover the shared secret
    using the receiver's private key.
    """
    shared_secret = ml_kem_768.decrypt(private_key, ciphertext)
    return shared_secret