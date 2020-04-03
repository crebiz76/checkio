def flat_list(array):
    # Start of Code

    #case 6
    temp = []; ret = []; j = []
    cnt = 0
    print('array=', array)
    
    while True:
        for i in range(len(array)):
            j = array[i]
            if type(j) == list:
                print('NOK')
                temp += j
                cnt += 1
            else:
                print('OK')
                temp.append(j)

        if cnt == 0: break
        array = temp; temp = []
        cnt = 0
                    
    ret = temp
    print(temp)
    return ret
    # End of Code

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3] , "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4] , "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7] , "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1] , "Four"
    assert flat_list([[[[[[[[[4294967295]]]]]]]]]) == [4294967295] , "Fail case added"
    print('Done! Check it')