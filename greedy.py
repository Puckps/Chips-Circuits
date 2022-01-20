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
        min_distance = 100
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

        if closest_node != end_node:
            closest_node.set_occupied()
        self.path._path.append(closest_node.get_coords())
        return closest_node
    
