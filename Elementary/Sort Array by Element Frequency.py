# Sort Array by Element Frequency

# Sort the given iterable so that its elements end up in the decreasing frequency order, that is,
#  the number of times they appear in elements. If two elements have the same frequency, they
#  should end up in the same order as the first appearance in the iterable.

# Input: Iterable
# Output: Iterable

# Example:
# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

# Precondition: elements can be ints or strings

from collections import Counter


def frequency_sort(items):
    result = [item for items, c in Counter(
        items).most_common() for item in [items] * c]
    return result


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))