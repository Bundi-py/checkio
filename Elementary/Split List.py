def split_list(items: list) -> list:
    sp1 = []
    sp2 = []

    if len(items) % 2 == 0:
        a = int(len(items) / 2)
        sal = items[:a]
        sa2 = items[a:]
        return [sal, sa2]
    else:
        b = int(len(items) / 2) + 1
        sbl = items[:b]
        sb2 = items[b:]
        return [sbl, sb2]


if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6, 7]))
