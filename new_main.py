from load import import_gates, get_dimensions, import_paths
from functions import get_neighbours, fastest_path
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors

class Node():
    def __init__(self, coordinate, id, is_nogate):
        self.coordinate = coordinate          # x, y, z 
        self.id = id
        self.is_nogate = is_nogate
        self.is_gate = False                  # true als node is a gate
        self.neighbours = []                  # all neigbouring nodes for given node

    def is_gate(self):
        self.is_gate = True

    def create_gate(self):
        self._gate = Gate(self.coordinate, self.id)

    def get_gate(self):
        return self._gate

class Gate():
    def __init__(self, coordinate, id):
        self.coordinate = coordinate
        self.id = id
# add
class Path():
    ''' Path object contains the begin-node and end-node from the netlist'''
    def __init__(self, gate_nodes, net):
        self.gate_nodes = gate_nodes
        self.net = net

# add
# import data on gates that have to be connected
gate_connections = import_paths("netlist_1.csv")

# import the data of the gates 
x_y = import_gates("print_0.csv")

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
        # if coordinate has a gate, nodes gets the id
        if coordinate in coordinates_gate.values():
            id = get_key(coordinate)
            nodes.append(Node(coordinate, id, False))
        # if coordinate is empty, nodes get id 0
        elif coordinate not in coordinates_gate.values():
            nodes.append(Node(coordinate, 0, True))

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
    if node.is_nogate == False:
        gate_nodes.append(node)

# add
# create list of objects that have to be connected
list_connections = []
empty_net = []
for list_item in gate_connections:
    empty_list = []
    # add first gate
    for node in gate_nodes:
        if node.id == list_item[0]:
            empty_list.append(node)
    # add second gate
    for node in gate_nodes:
        if node.id == list_item[1]:
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
for i in nodes:
    if i.id != 0:
        ax.scatter(i.coordinate[0], i.coordinate[1], 0) # plots the gates

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