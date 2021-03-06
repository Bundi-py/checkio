# You’ve received a letter from a friend whom you haven't seen or heard from for a while.
# In this letter he gives you instructions on how to find a hidden treasure.

# In this mission you should follow a given list of instructions which will get you to a certain
# point on the map. A list of instructions is a string, each letter of this string points you
# in the direction of your next step.

# The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

# It means that if the list of your instructions is "fflff" then you should move forward two times,
# make one step to the left and then again move two times forward.

# Now, let's imagine that you are in the position (0,0). If you move forward your position will
# change to (0, 1). If you move again it will be (0, 2). If your next step is to the left then your
# position will become (-1, 2). After the next two steps forward your coordinates will be (-1, 4)

# Your goal is to find your final coordinates. Like in our case they are (-1, 4)

# Input: A string.
# Output: A tuple (or list) of two ints
# Precondition: only chars f,b,l and r are allowed


def follow(instructions):
    f = 0
    r = 0
    b = 0
    l = 0
    hor = 0
    vert = 0
    for i in instructions:
        if i == 'f':
            f += 1
        elif i == 'r':
            r += 1
        elif i == 'b':
            b -= 1
        elif i == 'l':
            l -= 1
        hor = r + l
        vert = f + b
    return (hor, vert)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
