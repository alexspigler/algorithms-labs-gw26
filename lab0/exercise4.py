a = 0


def power(b):
    if b == 0:
        p = 1
    else:
        p = a * power(b - 1)

    print(f"Intermediate result: {a}^{b}={p}")
    return p


a = 3
print(f"3^2 = {power(2)}")
print(f"3^4 = {power(4)}")

a = 2
print(f"2^8 = {power(8)}")

# making a global does not change the powers, because a is not in the recursion