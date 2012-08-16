from datetime import datetime
import hashlib
import random
import uuid


def get_date_seed():
    return datetime.now().isoformat()


def get_random_seed(bits=64, as_uuid=False):
    """
    Return a random long int with the provided bit length.
    """
    seed = random.getrandbits(bits)
    if as_uuid:
        seed = uuid.UUID(seed)
    return seed


def get_hashed_seed(data, hash_type="sha512", as_uuid=False):
    """
    Legal values for hash_type are:
        'md5','sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    """
    hasher = getattr(hashlib, hash_type)
    hashed = hasher(data.encode("utf-8")).hexdigest()
    if as_uuid:
        hashed = uuid.UUID(hashed)
    return hashed


def get_super_seed():
    hashed = get_hashed_seed(
        get_date_seed() + str(get_random_seed()), hash_type="md5")
    return uuid.UUID(hashed)
