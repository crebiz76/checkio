def check_connection(network, first, second):
    print('================')
    cnt_net = 0; cnt_node = 0
    nets = []
    nodes_comb = set()
    result = []
    for node in network:
        cnt_net += 1
        nodes = node.split('-')
        nodes_comb.update(nodes)
        nets.append(node)
        cnt_node = len(nodes_comb)
    print('Nets =', cnt_net, nets)
    print('Nodes =', cnt_node, nodes_comb)
    
    netset = {}; netsets = set()
    temp = []; result = []; retval = False

    fnet = []; snet = []

    for net in nets:
        print(net)
        if first in net:
            fnet.append(net)
        if second in net:
            snet.append(net)

        print('first=', fnet, 'second=', snet)
        '''
        if netsets & netset == set():
            netsets = netset
            print('Network Changed...')
            result.append(temp)
        else:
            netsets = netsets | netset
            print('Network added...')
            temp = list(netsets)
        print('netsets=', netsets)
    
        if temp == []: result.append(list(netsets))
        else: result.append(temp)
        print('temp=', temp)
        '''
        
    print('result=', result, len(result))
    
    
    # check the network

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
