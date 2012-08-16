from datetime import datetime
import hashlib
import random


def get_date_seed():
    return datetime.now().isoformat()


def get_random_seed(bits=64):
    """
    Return a random long int with the provided bit length.
    """
    return random.getrandbits(bits)


def make_hashed_seed(data, hash_type="sha512"):
    """
    Legal values for hash_type are:
        'md5','sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    """
    hasher = getattr(hashlib, hash_type)
    return hasher(data.encode("utf-8")).hexdigest()
