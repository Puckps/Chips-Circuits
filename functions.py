import math

# get all neighbouring nodes of any node
def get_neighbours(current_node, nodes_list):
    neighbours = []
    x, y = current_node.coordinate
    possible_neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for node in nodes_list:
        if node.coordinate in possible_neighbours:
            neighbours.append(node)
    return neighbours

# get distance to any position
def get_distance(current_pos, direction):
        x1, y1 = current_pos
        x2, y2 = direction
        dx = x1 - x2
        dy = y1 - y2
        return math.sqrt(dx ** 2 + dy ** 2)

# calculate fastest path to end-node
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
            
