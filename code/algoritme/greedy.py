import classes
from code.functions.functions import manhattan_distance


class Greedy:
    """ Greedy pathfinding algorithm. """
    def __init__(self, path):
        self.path = path
        self.begin = self.path._net_gates[0]
        self.end = self.path._net_gates[1]

    def run_greedy(self):
        ''' Run Greedy algorithm. '''
        current_node = self.begin
        self.path._path.append(self.begin.get_coords())
        while current_node != self.end:
            current_node = self.closest_node(current_node, self.end)
        return

    def closest_node(self, current_node, end_node):
        ''' Continuously find closest node until end-node is reached. '''
        min = 1000
        best_node = current_node

        # check if node is not end-node
        if current_node.neighbour_end(end_node):
            for neighbour in current_node.get_neighbours():
                if neighbour == end_node:
                    best_node = neighbour
        # retrieve node closest to end-node
        else:
            for neighbour in current_node.possible_neighbours():
                dis = manhattan_distance(neighbour, end_node)
                if dis < min:
                    min = dis
                    best_node = neighbour

            if best_node == current_node:
                for neighbour in current_node._neighbours:
                    dis = manhattan_distance(neighbour, end_node)
                    if neighbour.has_gate() == False:
                        if dis < min:
                            min = dis
                            best_node = neighbour
                    else:
                        if dis < min:
                            min = dis
                            best_node = neighbour
        # set selected node as occupied
        if best_node != end_node:
            best_node.set_occupied()
        self.path._path.append(best_node.get_coords())
        return best_node
