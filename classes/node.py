from classes.gate import Gate 

class Node():
    ''' Node object containing gates, its neighbouring nodes, and A*-costs. '''
    def __init__(self, coordinate):
        self._coordinate = coordinate
        self._gate = False
        self._neighbours = []
        self._occupied = False
        self._f_cost = None
        self._h_cost = None
        self._g_cost = None
        self._parent = None

    def create_gate(self, id):
        ''' Put gate-object on Node. '''
        self._gate = Gate(self._coordinate, id)

    def get_gate(self):
        ''' Return the gate-object. '''
        return self._gate

    def get_coords(self):
        ''' Return node-coordinates. '''
        return self._coordinate

    def has_gate(self):
        ''' Check whether node contains gate. '''
        if self._gate != False:
            return True
        return False

    def create_neighbours(self, nodes_list):
        ''' Add neighbouring objects to current node's neighbours. '''
        neighbours = []
        x, y, z= self._coordinate
        possible_neighbours = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]
        for node in nodes_list:
            if node._coordinate in possible_neighbours:
                neighbours.append(node)
        self._neighbours = neighbours

    def get_neighbours(self):
        ''' Return neighbouring objects of current node. '''
        return self._neighbours
    
    def set_occupied(self):
        ''' Set node as occupied. '''
        self._occupied = True

    def possible_neighbours(self):
        ''' Return all unused neighbours. '''
        possible_neighbours = []
        for neighbour in self._neighbours:
            if neighbour._occupied == False:
                if neighbour.has_gate() == False:
                    possible_neighbours.append(neighbour)
        return possible_neighbours

    def neighbour_end(self, end_node):
        ''' Check if end-node has been reached. '''
        for neighbour in self._neighbours:
            if neighbour == end_node:
                return True
        return False