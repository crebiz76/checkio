def backward_string_by_word(text: str) -> str:
    # your code here
    temp = text
    word = temp.split()
    for i in word:
        k = ''
        for j in range(len(i)):
            k += i[-1-j]
        temp = temp.replace(i,k)
    print(text, '=>', temp)
    return temp


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
