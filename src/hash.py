import hashlib

ab_list = [
    [13, 17],
    [17, 23],
    [19, 29],
    [31, 17],
    [23, 31],
    [47, 41],
    [41, 13],
    [59, 7],
    [53, 29],
    [29, 43],
    [43, 19]
]


def hash(s, range, bucket):
    initial_seed = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)
    rand_for_bucket = initial_seed * ab_list[bucket][0] + ab_list[bucket][1]
    return rand_for_bucket % range
