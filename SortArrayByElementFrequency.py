'''
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Example:

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
1
2
Precondition: elements can be ints or strings

The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
'''

def frequency_sort(items):
    # your code here

    # Case-1
    '''
    #1. input
    itemlist = list(set(items))
    itemlist = []

    #2. processing
    print('==============================')
    for i in items:
        # 같은 엘리먼트의 갯수 확인
        j = items.count(i)
        # 같은 엘리먼트가 리스트에 없으면 
        if itemlist.count(i) == 0:
            # 엘리먼트의 갯수만큼 반복 
            for k in range(j):
                itemlist.append(i)
        # 출력
        print(i,j,k, itemlist)
    #3. output
    print('==============================')

    return itemlist
    '''
    # Case-2
    #0. analysis
    # 입력데이터 분석
    # - 중복값을 가지는 복수개의 list
    # 입력데이터의 중복 갯수를 확인
    # - 입력데이터를 Key값으로 중복 갯수를 Value로 Dictionary
    # 입력데이터 중 중복없는 값의 갯수를 확인(X)
    # - Dictionary를 만들어 중복 제거
    # 입력데이터 중 중복없는 값의 갯수만큼 출력
    # - 중복 갯수가 클수록 앞선다. 
    # - 중복 갯수가 같으면 먼저 입력된 값이 앞선다.  
    # - 중복 갯수의 비교는...
    #     

    #1. input
    itemtuple = {}
    itemlist = []
    for i in items:
        # 입력데이터의 중복 갯수를 확인
        j = items.count(i)
        # 입력데이터를 Key값으로 중복 갯수를 Value로 Dictionary
        itemtuple[i] = j
        print(i, j, itemtuple)
    
    k = {}
    
    # m.append([])

    cnt = 0
    for k in itemtuple:
        m = []
        m.append(k)        
        n = m * itemtuple.get(k)
        print(cnt, m, n)
        cnt = cnt + 1
    

    '''
    #2. processing
    print('==============================')
    for i in items:
        # 같은 엘리먼트의 갯수 확인
        j = items.count(i)
        # 같은 엘리먼트가 리스트에 없으면 
        if itemlist.count(i) == 0:
            # 엘리먼트의 갯수만큼 반복 
            for k in range(j):
                itemlist.append(i)
        # 출력
        print(i,j,k, itemlist)
    #3. output
    print('==============================')
    return itemlist
    '''


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
