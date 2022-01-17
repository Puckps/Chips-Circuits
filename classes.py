class Node():
    def __init__(self, coordinate):
        self.coordinate = coordinate            # x, y, z 
        self._gate = None                       # true als node is a gate
        self.neighbours = []                    # all neigbouring nodes for given node

    def create_gate(self, id):
        self._gate = Gate(self.coordinate, id)

    def get_gate(self):
        return self._gate

    def get_coords(self):
        return self.coordinate

class Gate():
    def __init__(self, coordinate, id):
        self.coordinate = coordinate
        self.id = id

    def get_coords(self):
        return self.coordinate

    def get_id(self):
        return self.id

# add
class Path():
    ''' Path object contains the begin-node and end-node from the netlist'''
    def __init__(self, gate_nodes, net):
        self.gate_nodes = gate_nodes
        self.net = net