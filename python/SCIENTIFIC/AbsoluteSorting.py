'''
len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
'''

def checkio(numbers_array: tuple) -> list:
    abs_num = []; retval = []
    for i in numbers_array:
        if i < 0:
            i = abs(i)
        abs_num.append(i)
    abs_num.sort()
    
    n = 0
    retval = abs_num
    for j in abs_num:
        for k in range(len(numbers_array)):
            if j == abs(numbers_array[k]):
                m = numbers_array[k]
        retval[n] = m
        n += 1
    return retval

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
