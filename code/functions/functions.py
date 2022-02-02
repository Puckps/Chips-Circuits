import math
import matplotlib.pyplot as plt
import numpy as np

def get_distance(current_pos, direction):
    ''' Get euclidian distance between any two points. '''
    x1, y1, z1 = current_pos
    x2, y2, z2 = direction
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    
def manhattan_distance(begin_node, end_node):
    ''' Get manhattan distance between any two points. '''
    x = begin_node.get_coords()[0] - end_node.get_coords()[0]
    y = begin_node.get_coords()[1] - end_node.get_coords()[1]
    z = begin_node.get_coords()[2] - end_node.get_coords()[2]

    manhattan_distance = abs(x) + abs(y) + abs(z)
    return manhattan_distance

def plot_graph(nodes, paths, max_x, max_y):
    ''' Plot figure of the gates in 3d-grid. '''
    fig = plt.figure(figsize=(max_x,max_y))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    ax.set_xlim([max_x, 0])
    ax.set_ylim([0, max_y])
    ax.set_zlim([0, 8])
    for node in nodes:
        if node.get_gate() != False:
            # plot the gates
            ax.scatter(node.get_coords()[0], node.get_coords()[1], 0)
            
    # plot all the nets from the path-class
    for path in paths:
        x, y, z = [], [], []
        for net in path._path:
            x.append(net[0])
            y.append(net[1])
            z.append(net[2])
            ax.plot(x,y,z)

    plt.savefig("output/representation.png")

def plot_2d(nodes, paths, max_x, max_y):
    ''' plot 2D layer of 3D grid. '''

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
            
    plt.savefig("output/2d_representation.png")

def get_key(val, dict):
    ''' Get key of dict by value. '''
    for key, value in dict.items():
         if val == value:
             return key            

def plot_hill_graph(hill_list):
    ''' Plot cost graph for hill climber. '''
    plt.clf()
    plt.plot(hill_list)
    plt.savefig("output/hill_graph.png")
