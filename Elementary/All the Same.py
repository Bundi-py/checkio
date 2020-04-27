# from typing import List, Any


# def all_the_same(elements: List[Any]) -> bool:
#     nlista = [elements[-1]]
#     for i in range(len(elements)):
#         if i in elements:
#             nlista.append(i)

#     if nlista == elements:
#         return True
#     else:
#         return False


# if __name__ == '__main__':
#     print("Example:")
#     print(all_the_same([1, 1, 1]))


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 0:
        return True

    for i in elements:
        if elements.count(i) == len(elements):
            return True
        return False


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
