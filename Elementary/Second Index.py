def second_index(text: str, symbol: str) -> [int, None]:
    a = text.replace(symbol, 'X', 1).find(symbol)
    if a == -1:
        return None
    else:
        return a


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))
