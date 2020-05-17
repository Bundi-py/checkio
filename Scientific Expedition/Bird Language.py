VOWELS = "aeiouy"


def translate(phrase):
    output = ""
    c = 0

    while c < len(phrase):
        output += phrase[c]
        if phrase[c] in VOWELS:
            c = c + 3
        elif phrase[c] == ' ':
            c = c + 1
        else:
            c = c + 2

    return output


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
