from load import import_gates, get_dimensions
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node():
    def __init__(self, coordinate, id, is_nogate):
        self.coordinate = coordinate          # x, y, z 
        self.id = id
        self.is_nogate = is_nogate
        self.is_gate = False                  # true als node is a gate

    def is_gate(self):
        self.is_gate = True

# import the data of the gates 
x_y = import_gates("print_2.csv")

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

print(len(nodes))            
for i in nodes:
    print(i.coordinate)
    print(i.id)

# plots a figure of the gates in a 3d grid
fig = plt.figure(figsize=(max_x,max_y))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([max_x, 0])
ax.set_ylim([0, max_y])
ax.set_zlim([0, 8])
for i in nodes:
    if i.id != 0:
        ax.scatter(i.coordinate[0], i.coordinate[1], 0) # plots the gates

plt.savefig('representation.png')