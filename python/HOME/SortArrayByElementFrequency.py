def frequency_sort(items):
    # your code here
    print('items=', items)

    a = []
    for i in items: 
        if not i in a: 
            a.append(i)
    print('a=', a)
    
    cnt = 0
    temp = []
    for j in items: 
        cnt = items.count(j)
        temp.append(cnt)
    temp.sort()
    temp.reverse()
    print('temp=', temp)

    ret = []
    for k in temp:
        for m in a:
            if k == items.count(m) and k > ret.count(m):
                ret.append(m)
                print('k=', k, 'm=', m, 'ret=', ret)
                break
    print('ret=', ret)
    return ret

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
    print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")