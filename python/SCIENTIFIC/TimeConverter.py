def time_converter(time):
    #replace this for solution
    
    #1. input
    strtime = time.split(':')

    #2. processing
    inttime = int(strtime[0])
    
    if inttime < 12:
        ampm = 'a.m.'
    else:
        ampm = 'p.m.'
    
    if inttime == 0: 
        inttime = 24
        
    if inttime > 12:
        inttime = inttime - 12
        
    #3. output
    time = str(inttime) + ':' + strtime[1] + ' ' + ampm

    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")