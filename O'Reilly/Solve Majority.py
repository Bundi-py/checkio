def is_majority(items: list) -> bool:
    t = 0
    for i in items:
        if i == True:
            t += 1
    if t > len(items) / 2:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))
