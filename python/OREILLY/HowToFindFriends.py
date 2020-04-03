def check_connection(network, first, second):
    
    nets = []; netset = {}; netsets = set()
    temp = []; result = []; retval = False

    for net in network:
        nets = net.split('-')
        netset = set(nets)
        print(nets, netset)
        
        if netsets & netset == set():
            netsets = netset
            print('Network Changed...')
            result.append(temp)
        else:
            netsets = netsets | netset
            print('Network added...')
            temp = list(netsets)
        print('netsets=', netsets)

    if temp == []: result = [list(netsets)]
    else: result.append(temp)
    print('temp=', temp)
    print('result=', result)

    for i in result:
        if first in i and second in i:
            retval = True
    print(retval)
    return retval  

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
    assert check_connection(
        ("night-nikola",),"nikola","night") == True, "test"
    assert check_connection(
        ("dr101-mr99","mr99-out00","dr101-out00","scout1-scout2",
        "scout3-scout1","scout1-scout4","scout4-sscout","sscout-super",),
        "dr101","sscout") == False, "Basic-Test3"
    assert check_connection(
        ("nikola-robin","batman-nwing","mr99-batman","mr99-robin",
        "dr101-out00","out00-nwing",),
        "dr101","mr99") == True, "Extra-Test3"