from classes.gate import Gate 


class Node():
    def __init__(self, coordinate):
        self._coordinate = coordinate            # x, y, z 
        self._gate = None                        # true als node is a gate
        self._neighbours = []                    # all neigbouring nodes for given node
        self._occupied = False

    def create_gate(self, id):
        self._gate = Gate(self._coordinate, id)

    def get_gate(self):
        return self._gate

    def get_coords(self):
        return self._coordinate

    def has_gate(self):
        if self._gate != None:
            return True
        return False

    def gen_neighbours(self, nodes_list):
        neighbours = []
        x, y, z= self._coordinate
        possible_neighbours = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]
        for node in nodes_list:
            if node._coordinate in possible_neighbours:
                neighbours.append(node)
        self._neighbours = neighbours

    def get_neighbours(self):
        return self._neighbours
    
    def set_occupied(self):
        self._occupied = True

    def possible_neighbours(self):
        possible_neighbours = []
        for neighbour in self._neighbours:
            if neighbour._occupied == False:
                if neighbour.has_gate() == False:
                    possible_neighbours.append(neighbour)
        return possible_neighbours

    def manhattan_distince(self, end_node):
        x1, y1, z1 = self._coordinate
        x2, y2, z2 = end_node
        x = x1 - x2
        y = y1 - y2
        z = z1 - z2

        manhattan_distance = abs(x) + abs(y) + abs(z)
        return manhattan_distance

    def neighbour_end(self, end_node):
        for neighbour in self._neighbours:
            if neighbour == end_node:
                return True
        return False