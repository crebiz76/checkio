'''
You are given a text, which contains different english letters and punctuation symbols. 
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". 
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. 
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Example:

checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"

How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. 
For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear. 
This is interesting stuff for language experts!

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105
'''

def checkio(text: str) -> str:
    
    #replace this for solution
    
    #You are given a text, which contains different english letters and punctuation symbols. 
    #You should find the most frequent letter in the text. The letter returned must be in lower case.
    #While checking for the most wanted letter, casing does not matter, so for the purpose of your search, 
    #"A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
    
    #0. Fetch the input data
    data = text
    print("The input is: ",data)

    #1. The letter change to lower
    low_data = data.lower()
    print("The lower is:", low_data) 
    
    #2. The special character omit
    # split_low = data.split(' ')
    # print("Spliting:", split_low)
    
    alpha_data = ''

    for i in low_data:
        if i >= 'a' and i <= 'z':
            alpha_data = alpha_data + i
            print ("The alphabet is: ", alpha_data) 
       

    print("The final is:", alpha_data)
    
    for j in alpha_data:
        alpha_data 
        print(j)


    # vac = low.split(' ')
    
    # #3. Sort 
    # #4. count
    # print("result =", vac)
    
    # a = list(text)
    # a.sort()    
    # print("a = ", a)
    
    # b = text.split(' ')
    # print("b = ",b)
    
    # c = set(text)
    # print("c = ",c)
    
    # d = text.lower()
    # print("d = ",d)
    
    
    return 'l'

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