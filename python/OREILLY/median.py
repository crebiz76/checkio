from typing import List

def checkio(data: List[int]) -> [int, float]:

    #replace this for solution
    length = 0; mid = 0; median = 0
    data.sort()
    length = len(data) % 2
    mid = int(len(data) / 2)
    if length == 1:
        median = data[mid]
    else:
        median = float((data[mid-1] + data[mid]) / 2)
    return median

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
