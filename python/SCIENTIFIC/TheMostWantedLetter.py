def checkio(text: str) -> str:
    
    #replace this for solution
    
    #You are given a text, which contains different english letters and punctuation symbols. 
    #You should find the most frequent letter in the text. The letter returned must be in lower case.
    #While checking for the most wanted letter, casing does not matter, so for the purpose of your search, 
    #"A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
    
        #1. Fetch the input data
    data = text
    #2. The letter change to lower
    datalower = data.lower()
    
    #3. The special character omit
    dataomit = ''
    for i in datalower:
        if i >= 'a' and i <= 'z':
            dataomit = dataomit + i
    #4. The list of data   
    datalist = []
    datalist = list(dataomit)
    datalist.sort()
    #5. Dictionary of data
    datadic = {}
    for i in datalist:
        datalist.count(i)
        datadic[i] = datalist.count(i)
    #6. Compare the counter    
    cnt = 0
    ret = ''
    for i in datadic:
        if datadic.get(i) > cnt:
            cnt = datadic.get(i)
            ret = i

    return ret

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")