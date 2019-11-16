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

    # Case-1: 오류있음(불완전한 코드)
    '''
    itemlist = list(set(items))
    itemlist = []

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
    
    print('==============================')
    return itemlist
    '''
    # Case-2
    print(items)    
    print('==============================')
    itemdict = {}
    itemlist = []
    for i in items:
        j = items.count(i)      # 입력데이터의 중복 갯수를 확인
        itemdict[i] = j         # 입력데이터를 Key값으로 갯수를 Value로 Dictionary
        itemlist.append(j)      # 입력데이터의 갯수를 리스트
        itemlist.sort()         # 입력 갯수 리스트를 순차로 정렬
        itemlist.reverse()      # 순차로 정렬된 리스트를 역순
        
    print(itemdict, itemlist)
    print('==============================')
    #print(itemlist)
    
    keyset = []
    valueset = []
    for key, value in itemdict.items(): 
        keyset.append(key)
        valueset.append(value)
    print('key=', keyset)
    print('value=', valueset)
    
    # itemset = []
    # for i in range(len(keyset)):
    #     temp = []
    #     temp.append(keyset[i])
    #     itemset.append(temp*valueset[i])
    # print('itemset=',itemset)

    #n = 0
    #for key,value in itemdict.items():
    # for key in itemdict.keys():
    #     fin = []
    #     fin.append(key)
    #     print(fin, value)
    #     fin*int(value)
    #     #n = n + 1
    #     print(fin)


    print(itemlist)
    return itemlist

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
    # print("Coding complete? Click 'Check' to earn cool rewards!")