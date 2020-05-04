# Sort the numbers in an array. But the position of zeros should not be changed.

# Input: A List.
# Output: An Iterable (tuple, list, iterator ...).

# Example:
# except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
# except_zero([0, 2, 3, 1, 0, 4, 5]) == [0, 1, 2, 3, 0, 4, 5]


from typing import Iterable


def except_zero(items: list) -> Iterable:
    new_list = []
    for i in items:
        if i != 0:
            new_list.append(i)
            new_list = sorted(new_list)

    for ind, numb in enumerate(items):
        if numb == 0:
            new_list.insert(ind, 0)
    return new_list


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))
