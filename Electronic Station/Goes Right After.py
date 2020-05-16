# In a given word you need to check if one symbol goes right after another.
# Cases you should expect while solving this challenge:
# If more than one symbol is in the list you should always count the first one
# one of the symbols are not in the given word - your function should return False;
# any symbol appears in a word more than once - use only the first one;
# two symbols are the same - your function should return False;
# if the first instance of the second symbol comes before the first one, that should return False
# the condition is case sensitive, which mease 'a' and 'A' are two different symbols.

# Input: Three arguments. The first one is a given string, second is a symbol that shoud go first, and the third is a symbold that should go after the first one.
# Output: A bool.


def goes_after(word: str, first: str, second: str) -> bool:
    ind = 0

    if first not in word or second not in word:
        return False
    elif first == second:
        return False
    elif word.count(first) == 1 and first == word[-1]:
        return False

    for i in word:
        if i == first:
            ind = word.index(i) + 1

    if word[ind] == second and second not in word[:ind]:
        return True
    else:
        False

    return False


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    assert goes_after('almaz', 'm', 'a') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
