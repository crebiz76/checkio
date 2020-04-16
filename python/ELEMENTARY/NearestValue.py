def nearest_value(values: set, one: int) -> int:
    # your code here
    ret = 0
    near = 0
    differ = []
    vallist = list(values)
    # print(values)
    for i in values:
        differ.append(abs(one - i))
    cnt = 0
    idlist = []
    near = differ[0]
    for j in range(len(differ)):
        if near > differ[j]:
            near = differ[j]
            idlist = []
            idlist.append(vallist[j])
        elif near == differ[j]:
            cnt += 1
            idlist.append(vallist[j])
    print(differ, near, cnt, idlist)
    
    if cnt > 1:
        ret = idlist[0]
        for k in idlist:
            if ret >= k: ret = k
                # print('ret=', ret)
    else: ret = idlist[0]
    # temp = differ.index(near)
    # ret = vallist[temp]
    print('Result=', ret)
    return ret

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    assert nearest_value({0,-2},-1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!")
