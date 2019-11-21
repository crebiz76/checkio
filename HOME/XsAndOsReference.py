from typing import List

def checkio(game_result: List[str]) -> str:

    temp = ''
    for i in game_result:
        temp += i
    print(temp)

    o_temp = []; x_temp = []; p_temp = []
    for j in range(len(temp)):
        if temp[j] == 'X':
            x_temp.append(int(j))
        elif temp[j] == 'O':
            o_temp.append(int(j))
        else:
            p_temp.append(int(j))
    print("X={} O={} P={}".format(x_temp, o_temp, p_temp))

    row1 = set([0,1,2])
    row2 = set([3,4,5])
    row3 = set([6,7,8])
    col1 = set([0,3,6])
    col2 = set([1,4,7])
    col3 = set([2,5,8])
    slash = set([2,4,6])
    bslash = set([0,4,8])

    x_set = set(x_temp)
    o_set = set(o_temp)
    p_set = set(p_temp)
    
    print('X={} O={} P={}'.format(x_set, o_set, p_set))
    
    x_cnt = 0; o_cnt = 0
    if x_set & row1 == row1: x_cnt += 1
    if x_set & row2 == row2: x_cnt += 1
    if x_set & row3 == row3: x_cnt += 1
    if x_set & col1 == col1: x_cnt += 1
    if x_set & col2 == col2: x_cnt += 1
    if x_set & col3 == col3: x_cnt += 1
    if x_set & slash == slash: x_cnt += 1
    if x_set & bslash == bslash: x_cnt += 1
    
    if o_set & row1 == row1: o_cnt += 1
    if o_set & row2 == row2: o_cnt += 1
    if o_set & row3 == row3: o_cnt += 1
    if o_set & col1 == col1: o_cnt += 1
    if o_set & col2 == col2: o_cnt += 1
    if o_set & col3 == col3: o_cnt += 1
    if o_set & slash == slash: o_cnt += 1
    if o_set & bslash == bslash: o_cnt += 1

    if x_cnt > o_cnt: result = "X"
    elif x_cnt < o_cnt: result = "O"
    else: result = "D"

    print(x_cnt, o_cnt, result)
    return result

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    assert checkio(["O..",
        "XOX",
        "..O"])
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")