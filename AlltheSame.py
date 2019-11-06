'''
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True
'''

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    
    a = set(elements)
    print(a)
    
    b = len(a)
    
    if b > 1:
        return 0
    else:
        return 1

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

    assert all_the_same([1,"a",1]) == False
    assert all_the_same([600000]) == True
    assert all_the_same([10000,99999]) == False

