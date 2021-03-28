def to_camel_case(name):
    #replace this for solution
    print(name)
    upperflag = 1
    ret = ''
    for i in name:
        if upperflag == 1:
            tmp = i.upper()
            upperflag = 0
        else:
            tmp = i            
        if i == '_':
            upperflag = 1
        else:
            ret += tmp 
    print(ret)
    return ret

if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")