import classes
from functions import get_distance

class Greedy:
    """
    greedy 
    """
    def __init__(self, path):
        self.path = path
        self.begin = self.path._net_gates[0]
        self.end = self.path._net_gates[1]

    def run_greedy(self):
        current_node = self.begin
        self.path._path.append(self.begin.get_coords())
        while current_node != self.end:
            current_node = self.closest_node(current_node, self.end)
        return

    def closest_node(self, current_node, end_node):
        min_distance = 100000
        closest_node = current_node
        for neighbour in current_node._neighbours:
            if neighbour._occupied == False:
                distance = get_distance(neighbour.get_coords(), end_node.get_coords())
                if neighbour.has_gate() == False:
                    if distance < min_distance:
                        min_distance = distance
                        closest_node = neighbour
                elif neighbour == end_node:
                    min_distance = distance
                    closest_node = neighbour
        
        if closest_node == current_node:
            for neighbour in current_node._neighbours:
                distance = get_distance(neighbour.get_coords(), end_node.get_coords())
                if neighbour.has_gate() == False:
                    if distance < min_distance:
                        min_distance = distance
                        closest_node = neighbour
                elif neighbour == end_node:
                    min_distance = distance
                    closest_node = neighbour
        #         else:
        #             if distance < min_distance:
        #                 min_distance = distance
        #                 closest_node = neighbour

        if closest_node != end_node:
            closest_node.set_occupied()
        self.path._path.append(closest_node.get_coords())
        return closest_node

    def node_closest(self, current_node, end_node):
        min = 1000
        best_node = current_node

        if current_node.neighbour_end(end_node):
            for neighbour in current_node.get_neighbours():
                if neighbour == end_node:
                    best_node = neighbour
        else:
            for neighbour in current_node.possible_neighbours():
                dis = neighbour.manhattan_distince(end_node.get_coords())
                if dis < min:
                    min = dis
                    best_node = neighbour

            if best_node == current_node:
                for neighbour in current_node._neighbours:
                    dis = neighbour.manhattan_distince(end_node.get_coords())
                    if neighbour.has_gate() == False:
                        if dis < min:
                            min = dis
                            best_node = neighbour

        if best_node != end_node:
            best_node.set_occupied()
        self.path._path.append(best_node.get_coords())
        return best_node