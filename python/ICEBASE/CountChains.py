'''
from typing import List, Tuple
import math

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    rad = 0.0
    # your code here
    circle = circles
    circle_count = len(circle)
    
    rad = Line(circle[0], circle[1])
    print(rad)        
    
    return 0


coord1 = (); coord2 = ();
def Line(a, b):    
    coord1 = a[:2]
    coord2 = b[:2]
    print(coord1, coord2)
    
    x1, y1 = coord1 # x1, y1 값을 정의
    print(x1, y1)
    x2, y2 = coord2 # x2, y2 값을 정의
    print(x2, y2)
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2, y1),2))    

if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''

from typing import List, Tuple
from math import sqrt

def count_chains(circles: List[Tuple[int, int, int]]) -> int:

    print()
    count = 0
    o = []
    x = []
    # your code
    for i in range(len(circles)):
        for j in range(i, len(circles)):
            if i == j: continue
            else:
                print('i=', i, 'j=', j)
                # print(circles[i][0], circles[i][1], circles[i][2])
                # print(circles[j][0], circles[j][1], circles[j][2])
                dist_x = (circles[i][0] - circles[j][0])**2
                dist_y = (circles[i][1] - circles[j][1])**2
                dist_rad = circles[i][2] + circles[j][2]
                dist = sqrt(dist_x + dist_y)
                
                print(dist_x, dist_y, dist, dist_rad)
                if dist < dist_rad:
                    count += 1
                    print('O')
                    # o.append([i, j])
                    o.append(i)
                    o.append(j)
                else: 
                    print('X')
                    # x.append([i, j])
                    x.append(i)
                    x.append(j)

    print('match=', o, len(o))
    print('match_set', set(o))
    print('unmatch=', x, len(x))
    print('count =', count)
    result = len(circles) - count
    print('result =', result)

    if len(set(o)) == 0:
        result = len(circles)
    else:
        result = len(circles) - len(set(o)) + 1

    print(result)
    return result


if __name__ == '__main__':
    # print("Example:")
    # print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    # assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    # assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    # assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    # assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
