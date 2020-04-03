def verify_anagrams(first_word, second_word):
    word1 = first_word.replace(" ", "")
    # first_word.strip()
    # first_word.lstrip(' ')
    # first_word.rstrip(' ')
    
    word2 = second_word.replace(" ", "")
    #second_word.strip()
    # second_word.lstrip(' ')
    # second_word.rstrip(' ')
    
    # print("1.", first_word, " 2.", second_word)
    # print("1.", word1, " 2.", word2)

    first = list(word1.lower())
    second = list(word2.lower())
    # print(first, second)

    for i in first:
        if i == ' ': first.remove(' ')
        # print("1st=", i, first)
    
    for j in second:
        if j == ' ': second.remove(' ')
        # print("2nd=", j, second)

    # print(first, second)

    temp = []
    for k in range(len(first)):
        if first[k] in second: 
            second.remove(first[k])
            temp.append(first[k])
        # print("i= ",k, temp, second)

    for l in range(len(temp)):
        if temp[l] in first:
            first.remove(temp[l])

    if len(first) > 0 or len(second) > 0:
        # print(False)
        return False
    else:
        # print(True)
        return True
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
    assert verify_anagrams("Hello", "Hell") == False, "Test Fail"
    assert verify_anagrams("  Hi  all  ", "all hi") == True, "Test Fail"