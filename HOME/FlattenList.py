'''
Input data: A nested list with integers.

Output data: The one-dimensional list with integers.

Example:

flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

How it is used: This concept is useful for parsing and analyzing files with complex structures and the task challenges your creativity in writing short code.

Precondition: 0 ≤ |array| ≤ 100
∀ x ∈ array : -232 < x < 232 or x is a list
depth < 10
'''

def flat_list(array):
    # Start of Code
    
    '''
    # case 1
    level = 1
    temp = []
    cnt = 0
    while cnt < 10:
        for i in range(len(array)):
            if type(array[i]) == int:
                cnt += 1
                temp.append(array[i])
            else:
                level += 1
                temp += array[i]
        print(temp, level)
        #if level == 0: break
    array = temp
    return array
    '''
    
    '''
    # case 2
    level = 1
    temp = []
    for i in range(len(array)):
        if type(array[i]) == int:
            temp.append(array[i])
        else:
            level += 1
            temp += array[i]
    array.append(temp)
    return array
    '''
    '''
    # case 3
    print(array)
    b = 0
    c = 0
    d = []
    for i in array:
        if type(i) != int:
            print('NOK')
            b = array.index(i)
            c = len(i)
            d = i 
            array.remove(d)
            print(b,c,d, array)
        else:
            print('OK')    
    for j in range(c):
        #idx = b + j
        #val = array[b][j]
        #print(idx, val)
        array.insert(b+j, d[j])
        print(array)
    '''

    '''
    # case 4
    idx = 0
    length = 0
    cnt = 0
    print('input length=', len(array))
    while 1:
        cnt = 0
        for i in array:
            if type(i) != int:
                if len(i) != 1: cnt = 0
                idx = array.index(i)
                length = len(i)
                print('wrong =', idx, length)
                temp = []
                temp = array[idx]
                array.remove(temp)
                print('remove=', temp, 'after=', array)                
            else:
                cnt += 1
                print(cnt)

        if cnt == len(array):
            print('OK')
            return array
            break
        else:
            for j in range(length):
                array.insert(idx+j, temp[j])
            print(array)
    '''

    # case 5
    print(array)
    string = str(array)
    print(string)
    string = str(string.split('['))
    string = str(string.split(']'))
    print(string)

    temp = []
    for i in string:
	    if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 45:
		    temp.append(int(i))
    print('ans=', temp)
    return temp
    # End of Code

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3] , "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4] , "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7] , "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1] , "Four"
    assert flat_list([[[[[[[[[4294967295]]]]]]]]]) == [4294967295] , "Fail case added"
    print('Done! Check it')