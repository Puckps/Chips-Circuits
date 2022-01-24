import csv
from functions import get_key
from classes.path import Path
from classes.node import Node


class Board():
    def __init__(self, gate_file, net_file):
        self._gates = self.import_gates(gate_file)
        self._dimensions = self.get_dimensions(self._gates)
        self._netlist = self.import_net(net_file)
        self._nodes = self.get_grid(self._dimensions)


        for node in self._nodes:
            node.gen_neighbours(self._nodes)

        self._paths = self.gen_path()


    def import_gates(self, net_file):
        ''' Get gate coordinates from print file. '''

        with open(net_file) as infile:
            reader = csv.reader(infile)
            next(reader)

            coords_dict = {}
            for line in reader:
                coords_dict[int(line[0])] = (int(line[1]), int(line[2]), 0)
        return coords_dict
    
    def get_dimensions(self, gate_dict):
        ''' Get highest x and y to infer grid size. '''
        max_x, max_y = 0, 0

        for gates in gate_dict.values():
            if gates[0] > max_x:
                max_x = gates[0]

            if gates[1] > max_y:
                max_y = gates[1]

        dimensions = max_x + 2, max_y + 2
        return dimensions

    def import_net(self, net_file):
        with open(net_file) as infile:
            reader = csv.reader(infile)
            next(reader)

            net_list = []
            for line in reader:
                net = (int(line[0]),int(line[1]))
                net_list.append(net)

        return net_list

    def get_grid(self, dimensions):
        node_list = []
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                for z in range(7):
                    coordinate = (x, y, z)
            
                    if coordinate in self._gates.values():
                        gate_id = get_key(coordinate, self._gates)
                    
                        new_node = Node(coordinate)
                        new_node.create_gate(gate_id)
                        node_list.append(new_node)
                        
                    elif coordinate not in self._gates:
                        new_node = Node(coordinate)
                        node_list.append(new_node)
        return node_list

    def get_gatenodes(self):
        gate_nodes = []
        for node in self._nodes:
            if node._gate != None:
                gate_nodes.append(node)
        return gate_nodes

    def gen_path(self):
        path_list = []
        gate_nodes = self.get_gatenodes()
        for list_item in self._netlist:
            netlist_gates = []
            # add first gate
            for node in gate_nodes:
                if node.get_gate().id == list_item[0]:
                    netlist_gates.append(node)
            # add second gate
            for node in gate_nodes:
                if node.get_gate().id == list_item[1]:
                    netlist_gates.append(node)
            # create path-object with two gates
            path_list.append(Path(netlist_gates))

        return path_list
    
    def calculate_costs(self):
        costs = 0
        for path in self._paths:
            costs += len(path._path) - 1
        total_cost = costs + 300*self.calc_intersections() + 500*self.calc_used_gate()
        print(f"cost = {costs}")
        print(f"intersections = {self.calc_intersections()}")
        print(f"gate = {self.calc_used_gate()}")
        print(f"totaal {total_cost}")
        return total_cost

    def calc_intersections(self):
        list_nodes = []
        for path in self._paths:
            for node in path._path[1:-1]:
                list_nodes.append(node)
        set_nodes = set(list_nodes)
        
        return (len(list_nodes) - len(set_nodes))

    def calc_used_gate(self):
        used_list = []
        for path in self._paths:
            for node in path._path[1:-1]:
                for cor in self._gates.values():
                    if cor == node:
                        used_list.append(node)
        return(len(used_list))     

    def check_gate(self, node):
        if node._gate != None:
            return True
    
    # def get_nodes(self):
    #     return self._nodes