from utils.key_loader import load_public_key, load_private_key

pub = load_public_key("rahul")
priv = load_private_key("rahul")

print("Public:", len(pub))
print("Private:", len(priv))