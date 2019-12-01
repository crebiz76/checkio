VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    # text.lower()
    print('text=', text)
    temp = ''; result = ''
    for i in text:
        temp = i.lower()
        if temp < 'a' or temp > 'z':
            result += temp
        print(i, temp)
    retval = len(result.strip())
    print('result=', retval)

    return retval

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    # assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
