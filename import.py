import csv

def import_gates(file):
    ''' Get gate coordinates from print file. '''

    with open(file) as infile:
        reader = csv.reader(infile)
        next(reader)

        gate_list = []
        for line in reader:
            coords = int(line[1]), int(line[2])
            gate_list.append(coords)

    return gate_list


def get_dimensions(gate_list):
    ''' Get highest x and y to infer grid size. '''

    max_x, max_y = 0, 0

    for gate in gate_list:
        if gate[0] > max_x:
            max_x = gate[0]

        if gate[1] > max_y:
            max_y = gate[1]

    return(max_x + 2, max_y + 2)


def create_grid(dimensions):
    ''' Create matrix of x width and y height. '''

    matrix = []

    for i in range(dimensions[1]):
        matrix.append((dimensions[0]) * [0])

    return matrix


gates = import_gates('print_0.csv')
# print(gates)
# print()

dimensions = get_dimensions(gates)
# print(dimensions)
# print()

grid_2D = create_grid(dimensions)

for coord in gates:
    grid_2D[coord[1]][coord[0]] = 1

grid_2D.reverse()

for line in grid_2D:
    print(line)
print()
