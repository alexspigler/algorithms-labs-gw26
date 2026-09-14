def make_blanks(n):
    return "  " * n


def factorial(n, level):
    print(f"{make_blanks(level)}Level {level}: n={n}")
    if n == 0:
        return 1

    return n * factorial(n - 1, level + 1)


print(f"3! = {factorial(3, 0)}")
print(f"5! = {factorial(5, 0)}")
print(f"5! x 3! = {factorial(3, 0) * factorial(5, 0)}")