FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    #replace this for solution
    n = number
    hund = 0; other_tens = 0; second_ten = 0; first_ten = 0
    temp = []; retval = ''
    if n >= 100:
        hund = n // 100
        print('100>=...', hund)
        n -= (hund * 100)
    else: 
        hund = 0
    temp.append(hund)
    if n >= 20:
        other_tens = n // 10
        print('20>=...', other_tens)
        n -= (other_tens * 10)        
    else:
        other_tens = 0
    temp.append(other_tens)

    if n >= 10:
        second_ten = n
        print('10>=...', second_ten)
    else:
        second_ten = 0
    temp.append(second_ten)
        
    if n < 10:
        first_ten = n
        print('10<...', first_ten)
    else:
        first_ten = 0
    temp.append(first_ten)
    
    print(hund, other_tens, second_ten, first_ten)
    print(n, temp)

    # for i in range(len(temp)):
    if hund > 0:        retval += FIRST_TEN[hund - 1] + ' ' + HUNDRED
    if temp[0] > 0 and (temp[1] > 0 or temp[2] > 0 or temp[3] > 0): retval += ' '
    if other_tens > 0:  retval += OTHER_TENS[other_tens - 2]
    if temp[1] > 0 and (temp[2] > 0 or temp[3] > 0): retval += ' '
    if second_ten > 0:  retval += SECOND_TEN[second_ten - 10]
    if temp[2] > 0 and temp[3] > 0:     retval += ' '
    if first_ten > 0:   retval += FIRST_TEN[first_ten - 1]
    # if last == 4:       retval += ' '
    # retval = str(FIRST_TEN[temp])
    # retval.strip(' ')
    print('Result=', retval)
    return retval

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')