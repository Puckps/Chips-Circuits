from code.functions.functions import manhattan_distance


class Path():
    ''' Path object contains the begin-node and end-node from the netlist'''
    def __init__(self, net_gates):
        self._net_gates = net_gates
        self._path = []

    def get_path(self):
        ''' Retrieve lists of coordinates in path. '''
        return self._path

    def optimal_path(self):
        ''' Retrieve manhattan distance between begin-and end-node. '''
        distance = manhattan_distance(self._net_gates[0], self._net_gates[1])
        return distance
