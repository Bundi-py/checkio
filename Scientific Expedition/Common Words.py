# Let's continue examining words. You are given two string with words separated by commas.
# Try to find what is common between these strings. The words are not repeated in the same string.

# Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

# Input: Two arguments as strings.
# Output: The common words as a string.

# Precondition:
# Each string contains no more than 10 words.
# All words separated by commas.
# All words consist of lowercase latin letters.

from birdseye import eye
@eye
def checkio(first, second):
    a = first.split(',')
    b = second.split(',')
    a = set(a)
    b = set(b)
    c = a.intersection(b)
    c = sorted(c)
    c = ','.join(c)
    return c


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello"  # , "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three",
                   "four,five,one,two,six,three") == "one,three,two", "1 2 3"
