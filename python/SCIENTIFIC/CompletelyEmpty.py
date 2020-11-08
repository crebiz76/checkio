def completely_empty(val):
    print()
    print("Input={}".format(val))
    temp = True
    if type(val) is not list:
        if bool(val) is not True:
            if val != 0:
                print('4. Result is True')
                return True
            elif type(val) is dict:
                print('3. Result is True')
                return True
            else:
                print('5. Result is False')
                return False
        else:
            if type(val) is int:
                print('6. Result is False')
                return False
            elif type(val) is dict:
                print('3. Result is True')
                return True
            elif type(val) is str:
                print('3. Result is True')
                return True
            elif type(val) == object:
                print('3. Result is True')
                return True
            else:
                print('7. Result is False')
                return False
    else:
        if len(val) == 0:
            if bool(val):
                print('1. Result is False')
                return False
            else:
                print('2. Result is True')
                return True
        else:
            for i in range(len(val)):
                print("Depth={}".format(val[i]))
                temp = temp and completely_empty(val[i])
            return temp

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    assert completely_empty([iter(())]) == True, "Failed case"
    print('Done')
