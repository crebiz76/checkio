VOWELS = "aeiouy"

def translate(phrase):
    print('bird: ',phrase)
    temp = phrase
    temp = temp.replace('aaa', 'A')
    temp = temp.replace('eee', 'E')
    temp = temp.replace('iii', 'I')
    temp = temp.replace('ooo', 'O')
    temp = temp.replace('uuu', 'U')
    temp = temp.replace('yyy', 'Y')
    temp = list(temp)

    result = ''
    for i in temp:
        if i == 'a': temp.remove('a')
        if i == 'e': temp.remove('e')
        if i == 'i': temp.remove('i')
        if i == 'o': temp.remove('o')
        if i == 'u': temp.remove('u')
        if i == 'y': temp.remove('y')

    for j in temp:
        result += j.lower()
    
    print(result) 
    phrase = result
    return phrase

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
