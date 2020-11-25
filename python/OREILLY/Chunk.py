from typing import Iterable

def chunking_by(items: list, size: int) -> Iterable:
    # your code here
    print("Input=", items)
    temp = []; result = []
    if len(items) > 0:
        for i in range(len(items)):
            if i % size == 0:
                if bool(temp) is True:
                    print("temp", temp)
                    result.append(temp)
                    temp = []
                    temp.append(items[i])
                else:
                    temp.append(items[i])
            else:
                temp.append(items[i])
        result.append(temp)
    else:
        result = items
        print("result", result)
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
