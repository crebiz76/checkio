def split_pairs(a):
    # your code here
    ret = []
    if len(a) != 0:
        if len(a)% 2 == 1:
            a += '_'
    # print(a)
    temp = ''
    for i in range(len(a)):
        if i % 2 == 0:
            temp = ''
            temp += a[i]
        elif i % 2 == 1:
            temp += a[i]
            ret.append(temp)
    print(ret)
    return ret


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
