def count_paths(num_rows, num_cols):
    # If either coordinate is zero, only one straight path remains.
    # Notice that this condition uses "or", not "and".
    if num_rows == 0 or num_cols == 0:
        return 1

    # Reduce the problem to two smaller problems.
    down_count = count_paths(num_rows - 1, num_cols)
    right_count = count_paths(num_rows, num_cols - 1)
    return down_count + right_count


for r, c in [(2,2)]:
    n = count_paths(r, c)
    print(f"r={r} c={c} => n={n}")


# and instead of or doesn't work, because then will go to negative numbers and hit max recursion