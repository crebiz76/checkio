VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}


def worth_of_words(words):
    #replace this for solution
    result = []
    for i in words:
        temp = []
        for j in i:
            k = int(VALUES.get(j))
            # print(i, j, k)
            temp.append(k)
            #print('temp=', temp)
        result.append(temp)
        #print('result=', result)

    sum = 0; worth = []
    for n in result:
        #print(n)
        sum = 0
        for m in n:
            sum += m
        #print('sum=', sum)
        worth.append(sum)
    #print(worth)
    
    last = 0; maximun = 0; ind = 0
    for x in range(len(worth)):
        if worth[x] > last: 
            maximun = worth[x]
            last = worth[x]
            ind = x
        else: 
            maximun = last
        #print(worth[x], maximun, ind)
    #print(words)
    print('-----------------')
    print(words[ind])
    return words[ind]

if __name__ == '__main__':
    print("Example:")
    print(worth_of_words(['hi', 'quiz', 'bomb', 'president']))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
    assert worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
    print("Coding complete? Click 'Check' to earn cool rewards!")
