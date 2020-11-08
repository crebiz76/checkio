def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    print(word)
    '''
    # Case 1
    start = 0
    result = False
    for i in word:
        if first in i:
            start = 1
        elif start == 1 and second in i:
            start = 0
            result = True
            break
        else:
            start = 0
            result = False
    return result 
    '''
    # Case 2
    id1 = 0
    id2 = 0
    result = False
    id1 = word.find(first)
    id2 = word.find(second)
    
    if id1 < id2 and (id2-id1) == 1:
        result = True
    return result

if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after("world","w","r") == False
    assert goes_after("almaz","m","a") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
