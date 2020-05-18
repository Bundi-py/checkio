# You are given a rhyme (a multiline string), in which lines are separated by "newline" (\n).
# Casing does not matter for your search, but whitespaces should be removed before your search.
# You should find the word inside the rhyme in the horizontal (from left to right) or vertical
# (from up to down) lines. For this you need envision the rhyme as a matrix (2D array). Find
# the coordinates of the word in the cut rhyme (without whitespaces).

# The result must be represented as a list -- [row_start,column_start,row_end,column_end], where
#     row_start is the line number for the first letter of the word.
#     column_start is the column number for the first letter of the word.
#     row_end is the line number for the last letter of the word.
#     column_end is the column number for the last letter of the word.
#     Counting of the rows and columns start from 1.

# Input: Two arguments. A rhyme as a string and a word as a string (lowercase).
# Output: The coordinates of the word.
# Precondition: The word is given in lowercase
# 0 < |word| < 10
# 0 < |rhyme| < 300


def checkio(text, word):
    novi = text.strip().replace(' ', '')
    reci = novi.split('\n')
    red = 1
    indeks = 1
    duzina = len(word)
    vert = ''

    for i in novi:
        indeks += 1
        if i == word[0]:
            if reci[red-1][indeks-1:indeks-1+duzina] == word:
                return [red, indeks, red, indeks+duzina-1]
                break
            else:
                for s in novi:
                    for t in s:
                        indeks += 1
                        if i == word[0]:
                            for v in range(len(word)):
                                vert += reci[red+v][indeks]
                                return [red, indeks, red, indeks+len(word)]
        if i == '\n':
            red += 1
            indeks = 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
    And dreaming often, dear,
    I dreamed that, if I counted all,
    -How many would appear?""", "ten") == [2, 14, 2, 16]
    # assert checkio("""He took his vorpal sword in hand:
    # Long time the manxome foe he sought--
    # So rested he by the Tumtum tree,
    # And stood awhile in thought.
    # And as in uffish thought he stood,
    # The Jabberwock, with eyes of flame,
    # Came whiffling through the tulgey wood,
    # And burbled as it came!""", "noir") == [4, 16, 7, 16]
