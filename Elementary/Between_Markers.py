# You are given a string and two markers (the initial and final). You have to find a
# substring enclosed between these two markers. But there are a few important conditions:

# The initial and final markers are always different.
# If there is no initial marker, then the first character should be considered the
# beginning of a string.
# If there is no final marker, then the last character should be considered the ending
# of a string.
# If the initial and final markers are missing then simply return the whole string.
# If the final marker comes before the initial marker, then return an empty string.

# Input: Three arguments. All of them are strings. The second and third arguments are
# the initial and final markers.
# Output: A string.

# import re


def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text:
        start = text.find(begin)+len(begin)
    else:
        start = len(text) - 1

    if end in text:
        kraj = text.find(end)+1
    else:
        kraj = len(text) - 1

    if start < kraj:
        substring = text[start:kraj-1]
    elif start > kraj:
        substring = text[:kraj]
    elif start == kraj:
        substring = ''
    return substring


if __name__ == '__main__':
    print('Example:')
    print(between_markers("<head><title>My new site</title></head>",
                          "<title>", "</title>"))
