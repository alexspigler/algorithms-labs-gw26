num_calls = 0
memory = {}

def count_paths(num_rows, num_cols):
    global num_calls
    num_calls += 1

    # If either coordinate is zero, only one straight path remains.
    # Notice that this condition uses "or", not "and".
    if num_rows == 0 or num_cols == 0:
        return 1
    if (num_rows, num_cols) in memory:
        return memory[(num_rows, num_cols)]

    # Reduce the problem to two smaller problems.
    down_count = count_paths(num_rows - 1, num_cols)
    right_count = count_paths(num_rows, num_cols - 1)
    memory[(num_rows, num_cols)] = down_count + right_count

    return down_count + right_count

for r, c in [(1, 1), (2, 2), (5, 7)]:
    num_calls = 0
    memory = {}
    n = count_paths(r, c)
    print(f"r={r} c={c} => n={n} num_calls={num_calls}")


# no memory:   r=5 c=7 => n=792 num_calls=1583
# memory:      r=5 c=7 => n=792 num_calls=81