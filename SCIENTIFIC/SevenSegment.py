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

def seven_disp(seg):
    ret = 0
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
    else:                           ret = 10
    return ret

def segment_case(seg):
    ret = []
    if seg == S1 or seg == s1:      ret = [1]
    elif seg == S2 or seg == s2:    ret = [2]
    elif seg == S3 or seg == s3:    ret = [1,3,7]
    elif seg == S4 or seg == s4:    ret = [4]
    elif seg == S5 or seg == s5:    ret = [5]
    elif seg == S6 or seg == s6:    ret = [5,6]
    elif seg == S7 or seg == s7:    ret = [1,7]
    elif seg == S8 or seg == s8:    ret = [0,1,2,3,4,5,6,7,8,9]
    elif seg == S9 or seg == s9:    ret = [1,3,4,5,7,9]
    elif seg == S0 or seg == s0:    ret = [0,1,7]
    else: ret = []
    return ret

def seven_segment(lit_seg, broken_seg):
    lit = lit_seg
    broken = broken_seg
    
    up = []; up_old = []; up_new = []
    low = []; low_old = []; low_new = []
    for seg in lit:
        if seg.islower():
            low.append(seg)
            low.sort()
        else:
            up.append(seg)
            up.sort()
    up_old = seven_disp(up)
    low_old = seven_disp(low)
    old = [seven_disp(up), seven_disp(low)]
    print('old=', up_old, low_old, old)
    
    for seg in broken:
        if seg.islower():
            low.append(seg)
            low.sort()
        else:
            up.append(seg)
            up.sort()
    up_new = seven_disp(up)
    low_new = seven_disp(low)
    new = [seven_disp(up), seven_disp(low)]
    print('new=', up_new, low_new, new)

    oldval = 0; newval = 0
    ret = []
    for i in range(len(new)):
        oldval = old[i]
        newval = new[i]
        print(oldval, newval)
        if newval == 10:
            newval = oldval
        if oldval == newval: ret.append(1)
        elif oldval == 0 and newval == 8: ret.append(2)
        elif oldval == 1 and newval == 3: ret.append(3)
        elif oldval == 1 and newval == 7: ret.append(2)
        elif oldval == 1 and newval == 9: ret.append(5)
        elif oldval == 5 and newval == 6: ret.append(2)
        elif oldval == 5 and newval == 8: ret.append(4)
        elif oldval == 10 and newval == 8: ret.append(10)
    
    result = ret[0] * ret[1]
    print(result)
    return result

if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4, 'Test - 0, 8, 80, 88'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    assert seven_segment(["A","B","C","b","c","f","g"],["G","d"]) == 1, 'fail'
    assert seven_segment([],["A","B","C","D","E","F","G","a","b","c","d","e","f","g"]) == 100, 'fail'
    assert seven_segment(["b","c","g","d","G","D","A","B"],["e","E","F","C","a"]) == 4, 'fail'
    print('"Run" is good. How is "Check"?')

''' Test 2
def seven_disp(seg):
    ret = 0
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
    else: ret = 10
    return ret, seg

def segment_case(seg):
    ret = []
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
    else: ret = []
    return ret

def seven_segment(lit_seg, broken_seg):
    segbefore = []; segafter = []
    low = []; up = []
    upcase = []; lowcase = []
    combine_low = []; combine_up = []

    segbefore = lit_seg
    for i in segbefore:
        if i.islower():
            low.append(i)
            low.sort()
        else:
            up.append(i)
            up.sort()

        upcase = seven_disp(up)
        lowcase = seven_disp(low)
        if lowcase != 10 and lowcase not in combine_low: combine_low.append(lowcase)
        if  upcase != 10 and  upcase not in combine_up: combine_up.append(upcase)
    print(up,low)
    print(combine_up, combine_low)
    
    # upcase = seven_disp(up)
    # lowcase = seven_disp(low)
    # combine_low.append(lowcase)
    # combine_up.append(upcase)

    segafter = broken_seg
    for j in segafter:
        if j.islower():
            low.append(j)
            low.sort()
        else:
            up.append(j)
            up.sort()     
        # LIST       
        upcase = seven_disp(up)
        lowcase = seven_disp(low)
        if lowcase != 10 and lowcase not in combine_low: combine_low.append(lowcase)
        if  upcase != 10 and  upcase not in combine_up: combine_up.append(upcase)
    print(up,low)
    print(upcase, lowcase)
    print('final=',combine_up, combine_low)
    
    #     SET
    #     upcase = seven_disp(up)
    #     lowcase = seven_disp(low)
    #     res1 = set(list(combine_low + lowcase))
    #     res2  = set(list(combine_up + upcase))
    # print('final=',res2, res1)    
    
    # digit = seven_disp(up) * 10 + seven_disp(low)
    result = len(combine_up) * len(combine_low)        
    print(result)
    #replace this for solution
    return result

if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4, 'Test - 0, 8, 80, 88'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
'''

''' Test 1
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
'''
