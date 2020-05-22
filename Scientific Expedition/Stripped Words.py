# Our robots are always working to improve their linguistic skills. For this mission, they
# research the latin alphabet and its applications.

# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels -- A E I O U Y
# Consonants -- B C D F G H J K L M N P Q R S T V W X Z

# You are given a block of text with different words. These words are separated by white-spaces
# and punctuation marks. Numbers are not considered words in this mission (a mix of letters and
# digits is not a word either). You should count the number of words (striped words) where the
# vowels with consonants are alternating, that is; words that you count cannot have two
# consecutive vowels or consonants. The words consisting of a single letter are not striped --
# do not count those. Casing is not significant for this mission.

# Input: A text as a string (unicode)
# Output: A quantity of striped words as an integer.
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    novi_txt = text.upper()
    novi_txt = re.split(r'[?,.\s]', novi_txt)
    novi_txt2 = [i for i in novi_txt if len(i) > 1]
    novi_txt2 = [i for i in novi_txt2 if i.isalpha()]

    novi_txt3 = []

    for i in novi_txt2:
        rec = ''
        if i[0] in VOWELS:
            for j, k in enumerate(i):
                if k in VOWELS and j % 2 == 0:
                    rec += k
                elif k in CONSONANTS and j % 2 == 1:
                    rec += k
            if rec == i:
                novi_txt3.append(i)

        elif i[0] in CONSONANTS:
            for j, k in enumerate(i):
                if k in CONSONANTS and j % 2 == 0:
                    rec += k
                elif k in VOWELS and j % 2 == 1:
                    rec += k
            if rec == i:
                novi_txt3.append(i)

    return len(novi_txt3)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio(
        "To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?") == 8
    print('If it is done - it is Done. Go Check it NOW!')


# Berislav:
# 1.

# def checkio(text):
#     count = 0
#     words = re.split(r'[?,.!\s]', text.upper())
#     for word in words:
#         if (len(word) <=1 or re.search(r'[0-9]', word)):
#             continue
#         valid_word = True
#         prev_ch = word[0]
#         for ch in word[1:]:
#             if ((ch in VOWELS and prev_ch in VOWELS) or (ch not in VOWELS and prev_ch not in VOWELS)):
#                 valid_word = False
#                 break
#             prev_ch = ch
#         if (valid_word):
#             count += 1
#     return count


#  2.
# def checkio(text):
#     count = 0
#     for word in re.split(r'[?,.!\s]', text.upper()):
#         if (len(word) <=1 or re.search(r'[0-9]', word)):
#             continue
#         if (not re.search('[AEIOYU]{2}', word) and not re.search('[BCDFGHJKLMNPQRSTVWXZ]{2}', word)):   #  [x]{2} = najmanje dva pojavljivanja znakova iz skupa [x]
#             count += 1
#     return count

# 3.
# def checkio(text):
#     count = 0
#     for word in re.split(r'[?,.!\s]', text.upper()):
#         if (len(word) > 1  and not re.search(r'[0-9]', word) and not re.search('[AEIOYU]{2}', word) and not re.search('[BCDFGHJKLMNPQRSTVWXZ]{2}', word)):
#             count += 1
#     return count
