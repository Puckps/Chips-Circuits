from code.functions.functions import get_distance, manhattan_distince


class Path():
    ''' Path object contains the begin-node and end-node from the netlist'''
    def __init__(self, net_gates):
        self._net_gates = net_gates
        self._path = []

    def shortest_path(self):
        print(self._net_gates)
        current_node = self._net_gates[0]
        
        new_node = current_node
        self._path = [current_node._coordinate]
        while current_node != self._net_gates[1]:
            min_distance = 10000
            for neighbour in current_node._neighbours:
                distance = get_distance(neighbour._coordinate, self._net_gates[1]._coordinate)
                if distance < min_distance:
                    min_distance = distance
                    new_node = neighbour
            current_node = new_node
            self._path.append(current_node._coordinate)  
        return self._path

    def get_path(self):
        return self._path