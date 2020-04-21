def caps_lock(text: str) -> str:
    # your code here
    caps = False
    result = ''
    for i in text:
        if i.isupper() == True:
            i = i
        elif caps == True:
            i = i.upper()
        elif caps == False:
            i = i.lower()
        
        if i == 'a' and caps == False:
            caps = True
        elif i == 'A' and caps == True:
            caps = False
        else:
            result += i
    print(result)
    return result

if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Madder than Mad Brian of Madcastle") == "MDDER THn MD BRIn of MDCstle"
    print("Coding complete? Click 'Check' to earn cool rewards!")
