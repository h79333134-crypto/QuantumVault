def load_public_key(user):
    with open(f"keys/{user}_public.key", "rb") as file:
        return file.read()


def load_private_key(user):
    with open(f"keys/{user}_private.key", "rb") as file:
        return file.read()