from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    if border not in items:
        return items
    elif len(items) == 0:
        return []
    else:
        for ind, num in enumerate(items):
            if num == border:
                end = ind + 1
                break

    return items[:end]


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))

    # ([1, 1, 5, 6, 7], 2)
    # ([1, 1, 2, 4, 2, 3, 4], 2)
    # ([1, 1, 2, 2, 3, 3], 2)
    # ([], 0)
