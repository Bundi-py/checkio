# You are given a list of files. You need to sort this list by file extension. The files with the same extestion should be sorted by name.
#
# Some possible cases:
# Filename cannot be an empty string;
# Files without extensions should go before the files with extensions;
# Filename ".config" has an empty extenstion and name ".config";
# Filename "config." has an empty extenstion and name "config.";
# Filename "table.imp.xls" has an extesntion "xls" and name "table.imp";
# Filename ".imp.xls" has extension "xls" and name ".imp".
#
# Input: A list of filenames.
# Output: A list of filenames.

import os
import string


def sort_by_ext(files):
    b = []
    for i in files:
        b.append(i.split('.'))
    # [['1', 'cad'], ['1', 'bat'], ['1', 'aa'], ['2', 'bat']]
    d = []
    for i in range(len(b)):
        d.append([b[i][1]] + [b[i][0]])
    # d = [['aa', '1'], ['bat', '1'], ['cad', '1'], ['bat', '2']]
    e = []
    e = sorted(d, key=lambda x: x[0])
    [['aa', '1'], ['bat', '1'], ['bat', '2'], ['cad', '1']]

    f = []
    for i in range(len(e)):
        f.append(e[i][1] + '.' + e[i][0])
    # f = ['1.aa', '1.bat', '2.bat', '1.cad']

    for i in range(len(f)):
        if f[i][0] == '.':
            a = f[i]
            f.remove(a)
            f.insert(0, a)
            # break

    return f


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == [
        '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == [
        '1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == [
        '.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == [
        '.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == [
        '1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")
