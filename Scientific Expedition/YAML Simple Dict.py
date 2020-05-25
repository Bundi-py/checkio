def yaml(a):
    recnik = {}
    a = a.split('\n')
    b = []
    c = []
    for i in a:
        if len(i) != 0:
            b.append(i)
    b = sorted(b)
    for i in b:
        c = i.split(':')
        recnik[c[0]] = c[1].strip()
    for k in recnik:
        if k == 'age':
            recnik[k] = int(recnik[k])
    return recnik


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
