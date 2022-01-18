from gate import Gate 


class Node():
    def __init__(self, coordinate):
        self._coordinate = coordinate            # x, y, z 
        self._gate = None                        # true als node is a gate
        self._neighbours = []                    # all neigbouring nodes for given node

    def create_gate(self, id):
        self._gate = Gate(self._coordinate, id)

    def get_gate(self):
        return self._gate

    def get_coords(self):
        return self._coordinate

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
