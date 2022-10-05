__author__ = 'kamta'


def create_seq(n):
    out = []
    while True:
        out.append(n)
        if n == 1:
            return out
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


def find_longest(n):
    n_seq = create_seq(n)
    max_len = 0
    val = n
    while n > 0:
        if n in n_seq:
            out_len = len(n_seq[n_seq.index(n):])
        else:
            out_len = len(create_seq(n))
        max_len = max(out_len, max_len)
        if max_len == out_len:
            val = n
        n -= 1
    return max_len, val
