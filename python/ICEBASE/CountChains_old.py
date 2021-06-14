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