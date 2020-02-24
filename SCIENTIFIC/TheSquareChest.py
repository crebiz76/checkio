from typing import List

one = [
        [[ 1, 2], [ 2, 6], [ 1, 5], [ 5, 6]],
        [[ 2, 3], [ 3, 7], [ 2, 6], [ 6, 7]],
        [[ 3, 4], [ 4, 8], [ 3, 7], [ 7, 8]],
        [[ 5, 6], [ 6,10], [ 5, 9], [ 9,10]],
        [[ 6, 7], [ 7,11], [ 6,10], [10,11]],
        [[ 7, 8], [ 8,12], [ 7,11], [11,12]],
        [[ 9,10], [10,14], [ 9,13], [13,14]],
        [[10,11], [11,15], [10,14], [14,15]],
        [[11,12], [12,16], [11,15], [15,16]],
      ]

two = [
        [[ 1, 2], [ 2, 3], [ 3, 7], [ 7,11], [ 1, 5], [ 5, 9], [ 9,10], [10,11]],
        [[ 2, 3], [ 3, 4], [ 4, 8], [ 8,12], [ 2, 6], [ 6,10], [10,11], [11,12]],
        [[ 5, 6], [ 6, 7], [ 7,11], [11,15], [ 5, 9], [ 9,13], [13,14], [14,15]],
        [[ 6, 7], [ 7, 8], [ 8,12], [12,16], [ 6,10], [10,14], [14,15], [15,16]]
      ]

three = [[ 1, 2], [ 2, 3], [ 3, 4], [ 4, 8], [ 8,12], [12,16], [ 1, 5], [ 5, 9], [ 9, 13], [13,14], [14, 15], [15, 16]]

def checkio(lines_list: List[List[int]]) -> int:
    count = 0
    result = 0; r1 = 0; r2 = 0; r3 = 0
    for i in lines_list:
        i.sort()
    lines_list.sort()
    print(lines_list)
    
    # print("One")
    for i in one:
        for j in i:
            # print(j)
            if j in lines_list:
                count += 1
        if len(i) == count:
            r1 += 1
        count = 0
    print("One=",r1)        
    
    # print("Two")
    for i in two:
        for j in i:
            # print(j)
            if j in lines_list:
                count += 1
        if len(i) == count:
            r2 += 1
        count = 0
    print("Two=",r2)
    
    # print("Three")
    for k in three:
        # print(k)
        if k in lines_list:
            count += 1
    if len(three) == count:
        r3 += 1
        count = 0
    print("Three=",r3)

    result = r1 + r2 + r3
    print("Result=",result)
    """Return the quantity of squares"""
    return result

if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                   [10, 14], [12, 16], [14, 15], [15, 16]]))

    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    assert (checkio([[16,15],[16,12],[15,11],[11,12],[11,10],[10,14],[9,10],[14,13],[13,9],[15,14]]) == 3), "Fail"
    print("Coding complete? Click 'Check' to earn cool rewards!")
