import math
import matplotlib.pyplot as plt
import numpy as np

# # get all neighbouring nodes of any node
# ### in nodes class
# def get_neighbours(current_node, nodes_list):
#     neighbours = []
#     x, y = current_node.coordinate
#     possible_neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
#     for node in nodes_list:
#         if node.coordinate in possible_neighbours:
#             neighbours.append(node)
#     return neighbours

# get distance to any position
### zegt iets over twee nodes, hulpfuctie of bij oath
def get_distance(current_pos, direction):
        x1, y1, z1 = current_pos
        x2, y2, z2 = direction
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

# calculate fastest path to end-node
### 
def fastest_path(begin_node, end_node):
    current_node = begin_node
    new_node = current_node
    net = [current_node.coordinate]
    while current_node != end_node:
        min_distance = 100
        for neighbour in current_node.neighbours:
            distance = get_distance(neighbour.coordinate, end_node.coordinate)
            if distance < min_distance:
                min_distance = distance
                new_node = neighbour
        current_node = new_node
        net.append(current_node.coordinate)
    return net

def plot_graph(nodes, paths, max_x, max_y):
    # plots a figure of the gates in a 3d grid
    fig = plt.figure(figsize=(max_x,max_y))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    ax.set_xlim([max_x, 0])
    ax.set_ylim([0, max_y])
    ax.set_zlim([0, 8])
    for node in nodes:
        if node.get_gate() != None:
            ax.scatter(node.get_coords()[0], node.get_coords()[1], 0) # plots the gates
            # plt.annotate(node.get_gate().id, (node.get_coords()[0], node.get_coords()[1]))
    # plot all the nets from the path-class
    for path in paths:
        x, y, z = [], [], []
        for net in path._path:
            x.append(net[0])
            y.append(net[1])
            z.append(net[2])
            ax.plot(x,y,z)

    plt.savefig("representation.png")

def plot_2d(nodes, paths, max_x, max_y):

    plt.figure(figsize=(max_x, max_y))

    plt.xticks(range(max_x))
    plt.yticks(range(max_y))
    plt.xlabel("X")
    plt.ylabel("Y")

    for node in nodes:
        if node.get_gate() != None:
            plt.scatter(node.get_coords()[0], node.get_coords()[1])
            plt.annotate(node.get_gate().id, (node.get_coords()[0], node.get_coords()[1]))

    for path in paths:
        x, y = [], []
        for net in path._path:
            x.append(net[0])
            y.append(net[1])
            plt.plot(x, y)
            
    plt.savefig("2d_representation.png")

# gets the key of a dict by value 
def get_key(val, dict):
    for key, value in dict.items():
         if val == value:
             return key            
