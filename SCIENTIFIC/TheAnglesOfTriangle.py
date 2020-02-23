from typing import List
import math

def checkio(a: int, b: int, c: int) -> List[int]:
    # inVal = [a, b, c]
    # inVal.sort()
    # print(inVal)
    
    # result = []
    # if inVal[0] == inVal[1] and inVal[1] == inVal[2]:
    #     result = [60, 60, 60]
    # elif inVal[2] >= inVal[1] + inVal[0]:
    #     result = [0, 0, 0]
    # else: 
    #     # result = [37, 53, 90]
    #     result = [0, 0, 90]
    #     deg1 = math.asin(inVal[0]/inVal[2])
    #     deg2 = math.asin(inVal[1]/inVal[2])
    #     result[0] = round(math.degrees(deg1))
    #     result[1] = round(math.degrees(deg2))
    #     print(result)
    '''
    a, b, c = length(m)
    A = angle(radian)
    a^2 = b^2 + c^2 -2*b*c*cos(A)
    '''
    result = []
    inVal = [a, b, c]
    inVal.sort()
    print(inVal)
    
    if inVal[2] >= inVal[1] + inVal[0]:
        result = [0, 0, 0]
    else: 
        A = math.acos((a**2 - b**2 - c**2)/(-2*b*c))
        B = math.acos((b**2 - a**2 - c**2)/(-2*a*c))
        C = math.acos((c**2 - a**2 - b**2)/(-2*a*b))
        
        degA = math.degrees(A)
        degB = math.degrees(B)
        degC = math.degrees(C)

        result.append(round(degA))
        result.append(round(degB))
        result.append(round(degC))

    #replace this for solution
    result.sort()
    print(result)
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio(4, 4, 4))

    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(11,20,30) == [11,20,149], "Failed"
    print("Coding complete? Click 'Check' to earn cool rewards!")