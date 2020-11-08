VOWELS = "AEIOUY".lower()
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ".lower()

def checkio(text):
    text = text.lower()
    # print('text=', text)

    table = str.maketrans('.,!?','    ')
    txt = text.translate(table)
    txt = txt.split()
    # print('txt=', txt)

    temp = ''; result = []
    isVowels = None
    for i in txt:
        for j in range(len(i)):
            if len(i) == 1:
                temp = ''
                isVowels = None
                break
            
            if i[j] < 'a' or i[j] > 'z':
                temp = ''
                isVowels = None
                break

            if i[j] in CONSONANTS:
                if isVowels is None:
                    isVowels = False
                    temp += i[j]
                elif isVowels is True:
                    isVowels = False
                    temp += i[j]
                else:
                    temp = ''
                    isVowels = None
                    break
            elif i[j] in VOWELS:
                if isVowels is None:
                    isVowels = True
                elif isVowels is False:
                    isVowels = True
                else:
                    temp = ''
                    isVowels = None
                    break
            # print("word={0}, char={1}, remain={2}".format(i,j,isVowels))
        
        result.append(temp)
        isVowels = None
        temp = ''
    # print(result)

    # return (len(result)-result.count(''))
    return len(' '.join(result).split())

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("""To take a trivial example, 
                    which of us ever undertakes laborious physical exercise, 
                    except to obtain some advantage from it?""") == 8,"Failed case"
    assert checkio("z") == 0, "Failed case"
    assert checkio("1st 2a ab3er root rate") == 1, "Failed case"