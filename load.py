import csv

def import_gates(file):
    ''' Get gate coordinates from print file. '''

    with open(file) as infile:
        reader = csv.reader(infile)
        next(reader)

        gate_list = []
        for line in reader:
            coords = int(line[0]), int(line[1]), int(line[2])
            gate_list.append(coords)

    return gate_list

def import_paths(file):
    ''' Retrieve gates that have to be connected'''

    with open(file) as infile:
        reader = csv.reader(infile)
        next(reader)

        path_list = []
        for line in reader:
            gates = (int(line[0]), int(line[1]))
            path_list.append(gates)
    
    return path_list


def get_dimensions(gate_list):
    ''' Get highest x and y to infer grid size. '''
    ## klopte nog niet helemaal nam namelijk de gate id inplaats van de x en daardoor nam hij de x als y
    ## kan nu dus ook zonder de +2 maar gwn de al bepaalde +1
    
    max_x, max_y = 0, 0

    for gate in gate_list:
        if gate[1] > max_x:
            max_x = gate[1]

        if gate[2] > max_y:
            max_y = gate[2]

    return(max_x + 1, max_y + 1)


def create_grid(dimensions):
    ''' Create matrix of x width and y height. '''

    matrix = []

    for i in range(dimensions[1]):
        matrix.append((dimensions[0]) * [0])

    return matrix

def get_netlist(file):

    with open(file) as infile:
        reader = csv.reader(infile)
        next(reader)

        net_list = []
        for line in reader:
            net = int(line[0]), int(line[1])
            net_list.append(net)

    return net_list

# gates = import_gates('print_0.csv')
# print(gates)
# print()

# dimensions = get_dimensions(gates)
# print(dimensions)
# print()

# grid_2D = create_grid(dimensions)

# for coord in gates:
#     grid_2D[coord[1]][coord[0]] = 1

# grid_2D.reverse()

# for line in grid_2D:
#     print(line)
# print()
