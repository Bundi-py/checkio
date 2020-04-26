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
        start = 0

    if end in text:
        kraj = text.find(end)
    else:
        kraj = len(text)

    if start < kraj:
        substring = text[start:kraj]
    elif start > kraj:
        substring = ''
    elif start == kraj:
        substring = ''
    return substring


if __name__ == '__main__':
    print('Example:')
    print(between_markers('No <hi>', '>', '<'))

    # print(between_markers('What is >apple<', '>', '<')# == "apple", "One sym"
    # print(between_markers("<head><title>My new site</title></head>",
    #                        "<title>", "</title>")# == "My new site", "HTML"
    # print(between_markers('No[/b] hi', '[b]', '[/b]')# == 'No', 'No opened'
    # print(between_markers('No [b]hi', '[b]', '[/b]') #== 'hi', 'No close'
    # print(between_markers('No hi', '[b]', '[/b]') #== 'No hi', 'No markers at all'
    # print(between_markers('No <hi>', '>', '<')# == '', 'Wrong direction'
