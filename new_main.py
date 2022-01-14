from load import import_gates, get_dimensions, import_paths
from functions import get_neighbours, fastest_path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from sys import argv

class Node():
    def __init__(self, coordinate):
        self.coordinate = coordinate          # x, y, z 
        self._gate = None                  # true als node is a gate
        self.neighbours = []                  # all neigbouring nodes for given node

    def create_gate(self, id):
        self._gate = Gate(self.coordinate, id)

    def get_gate(self):
        return self._gate

    def get_coords(self):
        return self.coordinate

class Gate():
    def __init__(self, coordinate, id):
        self.coordinate = coordinate
        self.id = id

    def get_coords(self):
        return self.coordinate

# add
class Path():
    ''' Path object contains the begin-node and end-node from the netlist'''
    def __init__(self, gate_nodes, net):
        self.gate_nodes = gate_nodes
        self.net = net

if len(argv) != 3:
    print("Usage: python3 filename main [gate file] [netist file]")
gate_file = f"{argv[1]}.csv"
net_file = f"{argv[2]}.csv"

# add
# import data on gates that have to be connected
gate_connections = import_paths(net_file)

# import the data of the gates 
x_y = import_gates(gate_file)

# import the dimensions
max_x = get_dimensions(x_y)[0]
max_y = get_dimensions(x_y)[1]

nodes = []
coordinates = []
coordinates_gate = {}
# list of nodes with gates on them
gate_nodes = []
# list of path-objects
paths = []


# gets the key of a dict by value 
def get_key(val):
    for key, value in coordinates_gate.items():
         if val == value:
             return key

# makes dict with id = key en coordinate = value
for j in x_y:
    coordinate_gate = j[1], j[2]
    #print(coordinate_gate)
    coordinates_gate[j[0]]= coordinate_gate


# creeets all coordinates on the chip
for i in range(max_x):
    for k in range(max_y):
        coordinate = (i, k)
        # if coordinate has a gate, node object gets gate object
        if coordinate in coordinates_gate.values():
            id = get_key(coordinate)
            new_node = Node(coordinate)
            new_node.create_gate(id)
            nodes.append(new_node)

        # if coordinate is empty, node object DOES NOT get gate object
        elif coordinate not in coordinates_gate.values():
            new_node = Node(coordinate)
            nodes.append(new_node)

# add
# add all the neighbouring nodes to all node objects
for node in nodes:
    neighbouring_nodes = get_neighbours(node, nodes)
    # do this so you don't get list in a list
    for i in range(len(neighbouring_nodes)):
        node.neighbours.append(neighbouring_nodes[i])

# add
# create list of all nodes with gates on them
for node in nodes:
    if node.get_gate() != None:
        gate_nodes.append(node)

# add
# create list of objects that have to be connected
list_connections = []
empty_net = []
for list_item in gate_connections:
    empty_list = []
    # add first gate
    for node in gate_nodes:
        if node.get_gate().id == list_item[0]:
            empty_list.append(node)
    # add second gate
    for node in gate_nodes:
        if node.get_gate().id == list_item[1]:
            empty_list.append(node)
    # create path-object with two gates
    paths.append(Path(empty_list, empty_net))

# add
# add nets to the path-objects
for path in paths:
    net = fastest_path(path.gate_nodes[0], path.gate_nodes[1])
    path.net = net
    print(path.gate_nodes[0].coordinate, path.gate_nodes[1].coordinate)
    print(path.net)

    
# plots a figure of the gates in a 3d grid
fig = plt.figure(figsize=(max_x,max_y))
ax = fig.add_subplot(111, projection='3d')
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_xlim([max_x, 0])
ax.set_ylim([0, max_y])
ax.set_zlim([0, 8])
for node in nodes:
    if node.get_gate() != None:
        ax.scatter(node.get_coords()[0], node.get_coords()[1], 0) # plots the gates

#cmap = colors.ListedColormap(['#ffffff', '#518c2a', '#ed2828', '#424141', '#4b87d1'])

# plot all the nets from the path-class
for path in paths:
    x, y, z = [], [], []
    for net in path.net:
        for coordinate in net:
            x.append(net[0])
            y.append(net[1])
            z.append(0)
        ax.plot(x,y,z)


plt.savefig('representation.png')