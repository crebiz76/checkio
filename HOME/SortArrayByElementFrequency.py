def frequency_sort(items):
    # your code here

    # Case-1: 오류있음(불완전한 코드)
    # itemlist = list(set(items))
    # itemlist = []

    # print('==============================')
    # for i in items:
    #     # 같은 엘리먼트의 갯수 확인
    #     j = items.count(i)
    #     # 같은 엘리먼트가 리스트에 없으면 
    #     if itemlist.count(i) == 0:
    #         # 엘리먼트의 갯수만큼 반복 
    #         for k in range(j):
    #             itemlist.append(i)
    #     # 출력
    #     print(i,j,k, itemlist)
    
    # print('==============================')
    # return itemlist
    
    # Case-2
    itemdict = {}
    itemlist = []
    for i in items:
        j = items.count(i)      # 입력데이터의 중복 갯수를 확인
        itemdict[i] = j         # 입력데이터를 Key값으로 갯수를 Value로 Dictionary
        itemlist.append(j)      # 입력데이터의 갯수를 리스트
        itemlist.sort()         # 입력 갯수 리스트를 순차로 정렬
        itemlist.reverse()      # 순차로 정렬된 리스트를 역순
        
    keyset = []
    valueset = []
    for key, value in itemdict.items(): 
        keyset.append(key)
        valueset.append(value)
    print('key=', keyset)
    print('value=', valueset)
    
    valueset.sort()
    print('sort value=', valueset)
    
    # for i in range(len(valueset)):
    #     for j in keyset:
    #         if valueset[i] == itemdict.get(j):
    #             print(i,j)
    result = []
    for i in valueset:
        temp = []
        char = ''
        for j in keyset:
            if i == itemdict.get(j) and itemlist.count(j) == 0: 
                char = 'o' 
                temp.append(j)
                itemlist = temp*int(i)
                break
            else:
                char = 'x'
            print(i, j, char, itemlist)
        if result != itemlist:
            result += itemlist


    # result = []
    # for i in keyset:
    #     temp = []
    #     for j in valueset:
    #         if j == itemdict.get(i) and temp == []:                
    #             temp.append(i)
    #             itemlist = temp*int(j)
    #             print(j, i, itemlist)
    #             break
    #     if result != itemlist:
    #         result += itemlist
    # print(result) 
    result.reverse()   
    return result

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")