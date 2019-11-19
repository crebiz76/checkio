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
    # level = 1
    # temp = []
    # cnt = 0
    # while cnt < 10:
    #     for i in range(len(array)):
    #         if type(array[i]) == int:
    #             cnt += 1
    #             temp.append(array[i])
    #         else:
    #             level += 1
    #             temp += array[i]
    #     print(temp, level)
    #     #if level == 0: break
    # array = temp
    # End of Code

    # level = 1
    # temp = []
    # for i in range(len(array)):
    #     if type(array[i]) == int:
    #         temp.append(array[i])
    #     else:
    #         level += 1
    #         temp += array[i]
    # array.append(temp)
    
    print(array)

    for i in array:
        if type(i) != int:
            #print('array[{}]'.format(i))
            print('NOK')
        else:
            print('OK')
    
    return array

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3] , "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4] , "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7] , "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1] , "Four"
    print('Done! Check it')