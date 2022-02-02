import random


def multi_swap(netlist, swaps):
    ''' Swap multiple netlist items. '''
    for i in range(swaps):
        number_1 = random.randrange(1, len(netlist))
        netlist[0], netlist[number_1] = netlist[number_1], netlist[0]
    return netlist


def reverse_netlist(netlist):
    ''' Return netlist in opposite direction. '''
    netlist.reverse()
    return netlist


def most_used_gate(netlist):
    ''' Find busiest gate in netlist. '''
    list_net = [item for t in netlist for item in t]

    my_dict = {i: list_net.count(i) for i in list_net}
    sorted_dict = {}
    sorted_keys = sorted(my_dict, key=my_dict.get)

    for w in sorted_keys:
        sorted_dict[w] = my_dict[w]
    most_list = [*sorted_dict.keys()]
    new_list = []
    for i in range(len(most_list) - 1):
        for j in range(len(netlist)):
            if most_list[i] in netlist[j] and netlist[j] not in new_list:
                new_list.append(netlist[j])

    netlist = new_list


def least_used_gate(netlist):
    ''' Find least busy gate. '''
    list_net = [item for t in netlist for item in t]

    my_dict = {i: list_net.count(i) for i in list_net}
    sorted_dict = {}
    sorted_keys = sorted(my_dict, key=my_dict.get)

    for w in sorted_keys:
        sorted_dict[w] = my_dict[w]
    least_list = [*sorted_dict.keys()]
    least_list.reverse()

    new_list = []
    for i in range(len(least_list) - 1):
        for j in range(len(netlist)):
            if least_list[i] in netlist[j] and netlist[j] not in new_list:
                new_list.append(netlist[j])

    netlist = new_list


def random_netlist(netlist):
    ''' Shuffle a netlist. '''
    random.shuffle(netlist)
    return netlist
