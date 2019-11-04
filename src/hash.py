import hashlib


def hash(s, range):
    return int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % range
