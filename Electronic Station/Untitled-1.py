def calculateSquare(n):
    return n*n


numbers2 = (5, 6, 7, 8)
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = list(result)
print(numbersSquare)


d = map(lambda x: x * 3, numbers)
print(list(d))
