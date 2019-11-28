def safe_pawns(pawns: set) -> int:

    pawn = list(pawns)
    result = []
    for i in pawn:
        temp = []
        x = ord(i[0])
        y = int(i[1])
        temp.append(x)
        temp.append(y)
        result.append(temp)
    
    cnt = 0; convlist = []; convset = {}
    for j in result:
        conv1 = []; conv2 = []
        leftx1 = j[0] -1
        leftx2 = j[0] + 1
        lefty = j[1] - 1
        conv1.append(leftx1)
        conv1.append(lefty)
        conv2.append(leftx2)
        conv2.append(lefty)
    
        if (conv1 in result) or (conv2 in result): 
            cnt += 1
    return cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")