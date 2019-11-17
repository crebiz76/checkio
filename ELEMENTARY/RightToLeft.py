def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    # result = ""
    # for i in phrases:
    #     print('init=',i)
    #     i.replace('right', 'left')
    #     result = i + ','
    #     print(result)
    # print(result)
    #result = ""
    
    t1 = list(phrases)
    t2 = []
    print(t1)
    for i in range(len(t1)):
        t2 = t1[i] + ','
    
    t2 = t2.replace("right", "left")
    print(t2)
    return (t2)

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
