def letter_queue(commands):
    temp = ''
    for i in commands:
        command = i.split()
        print(command)
        if command[0] == 'PUSH':
            temp += command[1]
        elif command[0] == 'POP':
            temp = temp[1:]
        else:
            print('NOTHING')
    print(temp)
    return temp

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"