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
        temp.append(hund)
        print('100>=...', hund)
        n -= (hund * 100)
    if n >= 20:
        other_tens = n // 10
        temp.append(other_tens)
        print('20>=...', other_tens)
        n -= (other_tens * 10)
    if n >= 10:
        second_ten = n
        temp.append(second_ten)
        print('10>=...', second_ten)
    else:
        first_ten = n
        temp.append(first_ten)
        print('10<...', first_ten)
    
    print(hund, other_tens, second_ten, first_ten)
    print(n, temp)

    # for i in range(len(temp)):
    if hund > 0:        retval += FIRST_TEN[hund - 1] + ' ' + HUNDRED + ' '
    if other_tens > 0:  retval += OTHER_TENS[other_tens - 2] + ' '
    if second_ten > 0:  retval += SECOND_TEN[second_ten - 10] + ' '
    if first_ten > 0:   retval += FIRST_TEN[first_ten - 1]
            
    # retval = str(FIRST_TEN[temp])
    retval.strip()
    print('Result=', retval)
    return retval

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    # assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    # assert checkio(212) == 'two hundred twelve', "5th example"
    # assert checkio(40) == 'forty', "6th example"
    # assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')