'''
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.
'''

'''
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
    
    
    '''    
    #======================================    
    a = False
    b = False
    c = False
    d = False
    i = 0
    
    for indata in elements:
		i += 1
		print(i, indata)
        
	
    if(i <= 2):
        d = True
    else:
        d = False
        

    if(indata == [] or i < 2):
        d = True
    else:
        d = False

        a = indata.pop()
        b = indata.pop()
        c = indata.pop()
    
    if((a == b) and (b==c)):
        d = True
    else:
        d = False
    
    print(d)
    return d

    #======================================
    d = input.count()
    print(d)
    if(input < 2):
        c = True
    else:
        if(input[0] == input[1]):
            a = True
            if(input[1] == input[2]):
                b = True
    #======================================
    if(input.index[0] != input.index[1]):
        a = False
    else:
        if(input.index[1] != input.index[2]):
            b = False
    print(a&b&c)
    return a & b & c
    '''
    
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
