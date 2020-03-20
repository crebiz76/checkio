def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    # your code here
    ret = 0
    buf = ''
    Max = 0
    linelist = list(line)
    for i in linelist:
        if i == buf:
            ret += 1
            if ret >= Max:
                Max = ret
        else:
            ret = 1
        buf = i
    
    if Max >= ret:
        print(Max)
        return Max
    else:
        print(ret)
        return ret

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')