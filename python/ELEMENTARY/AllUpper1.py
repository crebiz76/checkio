def is_all_upper(text: str) -> bool:
    # your code here
    ret = True
    for i in range(len(text)):
        if text[i] == ' ':
            ret = True
        elif text[i].isupper() == True:
            ret = True
        elif text[i].islower() == False:
            ret = True
        else:
            ret = False
    return ret


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    # extra
    assert is_all_upper("123") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
