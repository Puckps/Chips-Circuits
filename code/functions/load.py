import csv


def import_gates(net_file):
    ''' Get gate coordinates from print file. '''
    with open(net_file) as infile:
        reader = csv.reader(infile)
        next(reader)

        coords_dict = {}
        for line in reader:
            coords_dict[int(line[0])] = (int(line[1]), int(line[2]), 0)
    return coords_dict


def import_net(net_file):
    ''' Get netlist from netlist file. '''

    with open(net_file) as infile:
        reader = csv.reader(infile)
        next(reader)

        net_list = []
        for line in reader:
            net = (int(line[0]), int(line[1]))
            net_list.append(net)

    return net_list
