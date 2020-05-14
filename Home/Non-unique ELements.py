# Your optional code here
# You can import some modules or create additional functions

from collections import Counter, OrderedDict
import collections


def checkio(data: list) -> list:
    keep = {k for (k, v) in Counter(data).items() if v > 1}
    return [x for x in data if x in keep]


if __name__ == "__main__":
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [
        10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
