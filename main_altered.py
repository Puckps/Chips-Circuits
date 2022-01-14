from load import import_gates, get_dimensions, get_netlist
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import argv

class Node():
    def __init__(self, coords):
        self._coords = coords
        self._gate = None

    def create_gate(self, id):
        self._gate = Gate(self._coords, id)

    def get_gate(self):
        return self._gate

    def get_coords(self):
        return self._coords


class Gate():
    def __init__(self, coords, id):
        self._coords = coords
        self._id = id

    def get_coords(self):
        return self._coords

if len(argv) != 3:
    print("Usage: python3 filename main [gate file] [netist file]")
gate_file = f"data/{argv[1]}.csv"
net_file = f"data/{argv[2]}.csv"

# import the data of the gates 
x_y = import_gates(gate_file)

# import the dimensions
max_x = get_dimensions(x_y)[0]
max_y = get_dimensions(x_y)[1]

nodes = []
coordinates = []
coordinates_gate = {}

# gets the key of a dict by value 
def get_key(val):
    for key, value in coordinates_gate.items():
         if val == value:
             return key

# makes dict with id = key en coordinate = value
for j in x_y:
    coordinate_gate = j[1], j[2]
    # print(coordinate_gate)
    coordinates_gate[j[0]]= coordinate_gate

# creates all coordinates on the chip
for x in range(max_x):
    for y in range(max_y):
        coordinate = (x, y)
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

# print(len(nodes))            
# for i in nodes:
#     print(i.coordinate)
#     print(i.id)

# plots a figure of the gates in a 3d grid
fig = plt.figure(figsize=(max_x,max_y))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([max_x, 0])
ax.set_ylim([0, max_y])
ax.set_zlim([0, 8])
for node in nodes:
    if node.get_gate() != None:
        ax.scatter(node.get_coords()[0], node.get_coords()[1], 0) # plots the gates

plt.savefig('representation.png')