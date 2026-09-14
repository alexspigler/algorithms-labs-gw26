a = 0
b = 0


def power():
    global b

    if b == 0:
        p = 1
    else:
        b = b - 1
        p = a * power()

    print(f"Intermediate result: {a}^{b}={p}")
    return p


a = 3
b = 2
print(f"3^2 = {power()}")

b = 4
print(f"3^4 = {power()}")

a = 2
b = 8
print(f"2^8 = {power()}")

# end result is the same
# but intermediate values that are printed are not, because as a global, the recursion can't "remember" what value b was at each level