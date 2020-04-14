def end_zeros(num: int) -> int:
    # your code here
    str_n = str(num)
    cnt = 0
    for i in range(len(str_n)):
        if str_n[i] == '0':
            cnt += 1
        else:
            cnt = 0
    return cnt


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
