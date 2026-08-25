import random


def make_random_list(length):
    return [random.randint(1, 100) for _ in range(length)]


def search(values, value, index):
    # switched if statements:
    if values[index] == value:
        return True
    if index >= len(values):
        return False


    # Otherwise, search farther into the list.
    return search(values, value, index + 1)


test_data = make_random_list(10)
search_term = random.randint(1, 100)
found = search(test_data, search_term, 0)

print(test_data)
print(f"search_term={search_term}")
print(f"found={found}")

# switching doesn't work, because then we get an out of range, since it isn't stopped first when index increments too high