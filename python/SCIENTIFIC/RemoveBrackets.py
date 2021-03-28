def remove_brackets(line: str) -> str:
    # your code here
    print("Input:", line)
    max = len(line)
    top = 0
    cur = 0
    ret = ''
    # print(max, top, cur)
    stack = []
    for l in line:
        temp = []
        cur += 1
        if l == '(' or l == '{' or l == '[':
            # push 
            # print("Push - ", l)
            # open bracket
            top = cur
        elif l == ')' or l == '}' or l == ']':
            # pop
            # print("Pop - ", l)
            # print(top, line[top-1])
            if l == ')' and line[top-1] == '(': 
                temp.append(top)
                temp.append(cur)
                # close bracket
                if top > 0: top -= 1
            elif l == '}' and line[top-1] == '{': 
                temp.append(top)
                temp.append(cur)
                # close bracket
                if top > 0: top -= 1
            elif l == ']' and line[top-1] == '[': 
                temp = [top, cur]
                # close bracket
                if top > 0: top -= 1
            else:
                # if top < max: top += 1
                if top > 0: top -= 1
        if temp != []: stack += temp
        print(stack)
        stack.sort()
        # print(max, top, cur)
    for s in stack:
        ret += line[s-1]
    print("Output", ret)
    return ret

if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]' # Error
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'  # Error
    print("Coding complete? Click 'Check' to earn cool rewards!")
