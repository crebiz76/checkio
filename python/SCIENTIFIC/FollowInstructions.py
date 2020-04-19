def follow(instructions):
    # your code here
    x = 0
    y = 0
    for i in instructions:
        if i == 'f':
            y += 1
        elif i == 'b':
            y -= 1
        elif i == 'l':
            x -= 1
        elif i == 'r':
            x += 1

    position = (x, y)    
    print(instructions, position)
    return position

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
