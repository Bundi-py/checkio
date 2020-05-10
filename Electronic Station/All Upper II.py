def is_all_upper(text: str) -> bool:
    new = ''
    if len(text) == 0 or text.isspace():
        return False

    if text.isdigit() == True:
        return False

    for i in text:
        if i.islower() == True:
            return False

    for i in text:
        if i.isupper() or i.isdigit() == True:
            return True
            break

    for i in text:
        if i.isupper() == True or i == ' ':
            new += i
    if new == text:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    assert is_all_upper('DIGITS123') == True
    assert is_all_upper('123') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
