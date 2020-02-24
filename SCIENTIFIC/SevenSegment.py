S1 = [    'B','C'                ]
S2 = ['A','B',    'D','E',    'G']
S3 = ['A','B','C','D',        'G']
S4 = ['B',    'C',        'F','G']
S5 = ['A',    'C','D',    'F','G']
S6 = ['A',    'C','D','E','F','G']
S7 = ['A','B','C'                ]
S8 = ['A','B','C','D','E','F','G']
S9 = ['A','B','C','D',    'F','G']
S0 = ['A','B','C','D','E','F'    ]

s1 = [    'b','c'                ]
s2 = ['a','b',    'd','e',    'g']
s3 = ['a','b','c','d',        'g']
s4 = ['b',    'c',        'f','g']
s5 = ['a',    'c','d',    'f','g']
s6 = ['a',    'c','d','e','f','g']
s7 = ['a','b','c'                ]
s8 = ['a','b','c','d','e','f','g']
s9 = ['a','b','c','d',    'f','g']
s0 = ['a','b','c','d','e','f'    ]

ret = 0
def seven_disp(seg):    
    if seg == S1 or seg == s1:      ret = 1
    elif seg == S2 or seg == s2:    ret = 2
    elif seg == S3 or seg == s3:    ret = 3
    elif seg == S4 or seg == s4:    ret = 4
    elif seg == S5 or seg == s5:    ret = 5
    elif seg == S6 or seg == s6:    ret = 6
    elif seg == S7 or seg == s7:    ret = 7
    elif seg == S8 or seg == s8:    ret = 8
    elif seg == S9 or seg == s9:    ret = 9
    elif seg == S0 or seg == s0:    ret = 0
    return ret

def segment_case(seg):
    if seg == S1 or seg == s1:      ret = [1]
    elif seg == S2 or seg == s2:    ret = [2]
    elif seg == S3 or seg == s3:    ret = [1,3,7]
    elif seg == S4 or seg == s4:    ret = [4]
    elif seg == S5 or seg == s5:    ret = [5]
    elif seg == S6 or seg == s6:    ret = [5,6]
    elif seg == S7 or seg == s7:    ret = [1,7]
    elif seg == S8 or seg == s8:    ret = [0,1,2,3,4,5,6,7,8,9]
    elif seg == S9 or seg == s9:    ret = [1,3,5,7,9]
    elif seg == S0 or seg == s0:    ret = [0,1,7]
    return ret

lowercase = 0
def seven_segment(lit_seg, broken_seg):
    segment = []
    low = []; up = []
    upcase = []; lowcase = []

    segment = lit_seg | broken_seg
    for i in segment:
        if i.islower():
            low.append(i)
            low.sort()
        else:
            up.append(i)
            up.sort()
    print(up,low)

    upcase = segment_case(up)
    lowcase = segment_case(low)
    print(upcase, lowcase)

    # digit = seven_disp(up) * 10 + seven_disp(low)
    result = len(upcase) * len(lowcase)        
    print(result)
    #replace this for solution
    return result


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4, 'Test - 0, 8, 80, 88'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')

