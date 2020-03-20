# The list of banned words are as follows:
def checkio(data):
    if len(data)==0: return 0
    return data[0]+checkio(data[1:])

if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio([1, 2, 3]) == 6
    assert checkio([2, 2, 2, 2, 2, 2]) == 12
    print("Coding complete? Click 'Check' to earn cool rewards!")
