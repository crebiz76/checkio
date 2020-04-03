numeral = {'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000
           }


def checkio(data):
    print(data)
    ret = ''
    #replace this for solution
    temp = data % 4000
    m1000 = int(temp/1000)
    temp = temp%1000
    
    d500 = int(temp/500)
    temp = temp%500

    c100 = int(temp/100)
    temp = temp%100

    l50 = int(temp/50)
    temp = temp%50

    x10 = int(temp/10)
    temp = temp%10

    v5 = int(temp/5)
    temp = temp%5

    i1 = temp

    print(m1000, d500, c100, l50, x10, v5, i1)

    while m1000:    m1000 -= 1; ret = ret + 'M'
    while d500:     d500 -= 1;  ret = ret + 'D'
    while c100:     c100 -= 1;  ret = ret + 'C'
    while l50:      l50 -= 1;   ret = ret + 'L'
    while x10:      x10 -= 1;   ret = ret + 'X'
    while v5:       v5 -= 1;    ret = ret + 'V'
    while i1:       i1 -= 1;    ret = ret + 'I'
    
    print(ret)

    temp = ret
    if 'CCCC' in ret:
        temp = ret.replace('DCCCC','CM')
        temp = temp.replace('CCCC','CD')        
    if 'XXXX' in ret:
        temp = temp.replace('LXXXX','XC')
        temp = temp.replace('XXXX','XL')
    if 'IIII' in ret:
        temp = temp.replace('VIIII','IX')
        temp = temp.replace('IIII','IV')

    print(temp)
    ret = temp
    return ret

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio(3999) == "MMMCMXCIX", 'test fail'
    assert checkio(44) == "XLIV",'test fail'
