def popular_words(text: str, words: list) -> dict:
    recnik = {i: 0 for i in words}
    for i in text.lower().split():
        if i in recnik.keys():
            recnik[i] = recnik[i] + 1

    return recnik


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))
