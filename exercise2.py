def sum_to_n(n):
    if n == 0:
        return 0
    if n > 0:
        return n + sum_to_n(n - 1)
    else:
        raise ValueError("n must be > 0")

