from load import import_gates, get_dimensions, import_paths
from functions import get_neighbours, fastest_path, plot_graph, get_key
from sys import argv
import pandas as pd
from classes import Node, Path

if len(argv) != 3:
    print("Usage: python3 filename main [gate file nr] [netist file nr]")
gate_file = f"print_{argv[1]}.csv"
net_file = f"netlist_{argv[2]}.csv"

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


# makes dict with id = key en coordinate = value
for j in x_y:
    coordinate_gate = j[1], j[2]
    coordinates_gate[j[0]]= coordinate_gate

# creeets all coordinates on the chip
for i in range(max_x):
    for k in range(max_y):
        coordinate = (i, k)
        # if coordinate has a gate, node object gets gate object
        if coordinate in coordinates_gate.values():
            id = get_key(coordinate, coordinates_gate)
            new_node = Node(coordinate)
            new_node.create_gate(id)
            nodes.append(new_node)

        # if coordinate is empty, node object DOES NOT get gate object
        elif coordinate not in coordinates_gate.values():
            new_node = Node(coordinate)
            nodes.append(new_node)

# add all the neighbouring nodes to all node objects
for node in nodes:
    neighbouring_nodes = get_neighbours(node, nodes)
    # do this so you don't get list in a list
    for i in range(len(neighbouring_nodes)):
        node.neighbours.append(neighbouring_nodes[i])

# create list of all nodes with gates on them
for node in nodes:
    if node.get_gate() != None:
        gate_nodes.append(node)

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

net_list = []
path_list = []
length = 0
# add nets to the path-objects
for path in paths:
    net = fastest_path(path.gate_nodes[0], path.gate_nodes[1])
    path.net = net
    path_str = str(path.net).replace(" ", "")
    net_output = f"({int(path.gate_nodes[0].get_gate().id)},{int(path.gate_nodes[1].get_gate().id)})"
    net_list.append(net_output)
    path_list.append(path_str)
    length = length + len(path.net)
length = length - len(path_list)

df = pd.DataFrame({"net": net_list, "wires": path_list})
df2 = {"net": f"chip_{argv[1]}_net_{argv[2]}", "wires" : length}
df = df.append(df2, ignore_index=True)
df.to_csv("output.csv", index=False)

plot_graph(nodes, paths, max_x, max_y)