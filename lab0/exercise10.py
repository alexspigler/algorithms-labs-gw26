num_calls = 0


def fibonacci(n):
    global num_calls
    num_calls += 1

    if n <= 2:
        return n - 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for n in [5, 20]:
    num_calls = 0
    f = fibonacci(n)
    print(f"f({n}) = {f}    num_calls={num_calls}")

# recursion uses so many calls because the original n-1 and n-2 branches overlap yet don't share the answers/work