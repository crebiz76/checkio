def split_list(items: list) -> list:
    # your code here
    item_a = []; item_b = []
    division = len(items)//2
    remainder = len(items)%2

    item_a = items[:(division + remainder)]
    item_b = items[(division + remainder):]
    
    print(item_a, item_b)
    return [item_a, item_b]

if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
