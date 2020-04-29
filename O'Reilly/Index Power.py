def index_power(array: list, n: int) -> int:
    if n < 0:
        return '"IndexError"'
    else:
        for i, v in enumerate(array):
            if i == n:
                elem = i
                return array[i]**n


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], -1))
