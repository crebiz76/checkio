# sum
# import
# for
# while
# reduce

# addition = 'addition'
def checkio(data):
    print(data, len(data))
    cnt = 0; temp = 0

    label: addition
    if cnt < len(data):
        temp += data[cnt]
        cnt += 1
        goto: addition
    else:
        print(temp)
    return temp

checkio([1, 2, 3]) == 6
checkio([2, 2, 2, 2, 2, 2]) == 12

if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
    print("Coding complete? Click 'Check' to earn cool rewards!")