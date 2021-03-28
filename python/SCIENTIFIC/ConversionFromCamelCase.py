def from_camel_case(name):
    #replace this for solution
    ret = ''
    for i in name:
        if i.isupper():
            tmp = '_' + i.lower()
        else:
            tmp = i
        ret += tmp
    if(ret[0] == '_'):
        ret = ret[1:]
    return ret

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")