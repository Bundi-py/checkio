from collections import Counter


def checkio(data: list) -> list:
    counts = Counter(data)
    non_un = []
    for i in data:
        if counts[i] > 1:
            non_un.append(i)
    return non_un


if __name__ == "__main__":
    list(checkio([1, 2, 3, 1, 3]))  # == [1, 3, 1, 3], "1st example"
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert
    # assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    # assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    # assert list(checkio([10, 9, 10, 10, 9, 8])) == [
    #     10, 9, 10, 10, 9], "4th example"
