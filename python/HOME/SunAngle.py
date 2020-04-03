'''
Precondition:
00:00 <= time <= 23:59

Result:
06:00 - 0 deg
12:00 - 90 deg
18:00 - 180 deg
'''

def sun_angle(time):
    #replace this for solution
    print('Time=', time)
    degH = 15
    degM = 15/60

    Time = time.split(':')
    #print(Time)
    Hour = int(Time[0])
    Minute = int(Time[1])
    print(Hour, Minute)

    result = 0
    if Hour <= 5 or (Hour >= 18 and Minute >= 1):
        return "I don't see the sun!"
    else:
        result = (Hour - 6) * degH + Minute * degM
        return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")