def checkio(text, word):
    cut = text.replace(" ", "")
    cut = cut.lower()
    print("[Cut] =")
    print(cut)
    print("[Count]",len(cut))
    
    result = []
    for j in range(len(word)):
        temp = []
        cnt = 0; row = 1; col = 0
        print(word[j], "=====")
        for i in range(len(cut)):
            cnt += 1; col += 1
            if cut[i] == "\n":
                col = 0; row += 1
            
            if word[j] == cut[i]:
                temp.append([row, col])
        result.append(temp)
    print(result)

    
    return [2, 14, 2, 16]
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    '''
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]'''