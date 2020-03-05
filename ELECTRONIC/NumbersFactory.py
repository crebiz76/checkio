def checkio(number):
    #replace this for solution
    result = []
    ret = ''
    retval = 0
    N = int(number)
    print("Number=",N)


    while N >= 2:
        for i in range(N, 1, -1):
            #print('i=',i)
            if N % i == 0 and i < 10:
                print(i, '<=')
                temp = i
                result.append(temp)                
                break
            else:
                temp = N
        N = N//temp
        print('N=', N)
    result.sort()
    print(result)

    check = 1
    for i in result:
            check = check * i
            ret = ret + str(i)
            
    if check != number:
        retval = 0
        print(retval)
        return retval
    else:
        retval = int(ret)
        print(retval)
        return retval

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    assert checkio(560) == 2578, "Fail"
    assert checkio(3275) == 0, "Fail"
