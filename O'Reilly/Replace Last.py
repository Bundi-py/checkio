from typing import Iterable


def replace_last(items: list) -> Iterable:
    if len(items) == 1:
        return items
    else:
        items.insert(0, items.pop())
        return items


if __name__ == '__main__':
    print("Example:")
    print(list(replace_last([2, 3, 4, 1])))
