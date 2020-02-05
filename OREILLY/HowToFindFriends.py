def check_connection(network, first, second):
    # network = list(network)
    netlist = []
    node = []
    nodes = {}
    # print('network= ', network)
    for i in network:
        i = i.split('-')
        netlist.append(i)
        for j in range(len(i)):
            node.append(i[j])
    nodes = set(node)
    # print('node=', node)
    print('netlist= ', netlist)
    # print('nodes/count= ', nodes, len(nodes))
    temp = f'nodes/count={nodes}/{len(nodes)}'
    print(temp)
    print('1st=', first, '/2nd=', second)
    
    node1 = []; node2 = []; node_f = []; node_v = []
    for j in netlist:
        # node_f.append(j)
        node_f.append(j[0])
        node_f.append(j[1])
        print(node_f)

        if first in j and second in j:
            print('connect')
        elif first in j:
            print('1st')
            # node1.append(j)
            node1.append(j[0])
            node1.append(j[1])
            node_f.remove(j[0])
            node_f.remove(j[1])            
        elif second in j:
            print('2nd')
            # node2.append(j)            
            node2.append(j[0])
            node2.append(j[1])
            node_f.remove(j[0])
            node_f.remove(j[1])
        else:
            print('non')
            node_v.append(j[0])
            node_v.append(j[1])
            node_f.remove(j[0])
            node_f.remove(j[1])

    print('future=', node_f)
    print('node1= ', node1)
    print('node2= ', node2)
    print('visit=', node_v)
    
    return True or False


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