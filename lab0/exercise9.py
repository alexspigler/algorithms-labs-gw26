path_num = 0

def count_paths(num_rows, num_cols, partial_path):
    global path_num

    # Complete a path that has reached the top row.
    if num_rows == 0:
        final_path = partial_path
        for c in range(num_cols - 1, -1, -1):
            final_path += f" -> [0,{c}]"
        path_num += 1
        print(f"Path #{path_num}: {final_path}")
        return 1

    # Complete a path that has reached the first column.
    if num_cols == 0:
        final_path = partial_path
        for r in range(num_rows - 1, -1, -1):
            final_path += f" -> [{r},0]"
        path_num += 1
        print(f"Path #{path_num}: {final_path}")
        return 1

    # Otherwise, reduce the problem in both possible ways.
    down_path = partial_path + f" -> [{num_rows - 1},{num_cols}]"
    down_count = count_paths(num_rows - 1, num_cols, down_path)

    right_path = partial_path + f" -> [{num_rows},{num_cols - 1}]"
    right_count = count_paths(num_rows, num_cols - 1, right_path)

    return down_count + right_count


for r, c in [(1, 1), (2, 2)]:
    path_num = 0
    n = count_paths(r, c, f"[{r},{c}]")
    print(f"r={r} c={c} => n={n}")