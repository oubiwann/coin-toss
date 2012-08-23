from datetime import datetime
import hashlib
import random
import uuid


def get_namespace_uuid(namespace):
    hashed = hashlib.md5(namespace.encode("utf-8")).hexdigest()
    return uuid.UUID(hashed)


def get_date_seed():
    return datetime.now().strftime("%Y-%m-%d")


def get_datestamp_seed():
    return datetime.now().isoformat()


def get_namespace_seed(namespace, data):
    return uuid.uuid5(get_namespace_uuid(namespace), data)


def get_random_seed(bits=128, as_uuid=False):
    """
    Return a random long int with the provided bit length.

    If you want a UUID, you should make sure your bits are 128.
    """
    seed = random.getrandbits(bits)
    if as_uuid:
        seed = uuid.UUID(int=seed)
    return str(seed)


def get_hashed_seed(data, hash_type="sha512", as_uuid=False):
    """
    Legal values for hash_type are:
        'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    """
    hasher = getattr(hashlib, hash_type)
    hashed = hasher(data.encode("utf-8")).hexdigest()
    if as_uuid:
        hashed = uuid.UUID(hashed)
    return str(hashed)
