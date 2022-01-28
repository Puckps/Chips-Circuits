import classes.board as brd
from functions import get_distance, manhattan_distince

class A_star:
    """
    A* algorithm
    """
    def __init__(self, path):
        self.path = path
        self.begin_node = self.path._net_gates[0]
        self.end_node = self.path._net_gates[1]
    

    def run_a_star(self):
        open_nodes = []
        closed_nodes = []
        self.calculate_f_cost(self.begin_node)
        open_nodes.append(self.begin_node)

        while len(open_nodes) > 0:
            # retrieve node with lowest f-cost.
            current_node = open_nodes[0]
            for node in open_nodes:
                # get node in the open-list with lowest f-cost or, in case of equal f-costs, lowest h-cost
                if node._f_cost < current_node._f_cost or (node._f_cost == current_node._f_cost and node._h_cost < current_node._h_cost):
                    current_node = node
            
            # remove current-node from open and put in closed
            open_nodes.remove(current_node)
            closed_nodes.append(current_node)

            # in case the end-node has been reached
            if current_node == self.end_node:
                path_nodes = self.retrace_path()
                self.remove_neighbours(path_nodes)
                self.set_as_occupied(path_nodes)
                self.reset_costs(open_nodes, closed_nodes)
                #print(len(closed_nodes), len(open_nodes))
                return
            
            # check if neighbours are traversable
            for neighbour in current_node._neighbours:
                if neighbour in closed_nodes or (neighbour.has_gate() and neighbour != self.end_node and neighbour != self.begin_node):
                    continue
                
                # check whether new path to neighbour is shorter or if neighbour is not yet in the open-list
                NewMovementCostToNeighbour = current_node._g_cost + manhattan_distince(current_node, neighbour)
                if neighbour._occupied == True:
                    NewMovementCostToNeighbour += 300
                if (neighbour._g_cost != None and NewMovementCostToNeighbour < neighbour._g_cost) or neighbour not in open_nodes:
                    neighbour._g_cost = NewMovementCostToNeighbour
                    neighbour._h_cost = manhattan_distince(neighbour, self.end_node)
                    neighbour._f_cost = neighbour._g_cost + neighbour._h_cost
                    neighbour._parent = current_node
                    
                    # if neighbour not in open-list, add it
                    if neighbour not in open_nodes:
                        open_nodes.append(neighbour)

    def retrace_path(self):
        path = []
        current_node = self.end_node

        # keep adding parents until path is complete
        while current_node != self.begin_node:
            path.append(current_node)
            current_node = current_node._parent
        
        # reverse the path to get begin-end
        path.append(self.begin_node)
        path.reverse()

        # return list of nodes that make up the final path
        return path
    
    def set_as_occupied(self, path_nodes):
        """Set all the nodes in list as occupied for next paths and put coordinates of nodes in the path-net"""
        for node in path_nodes:
            self.path._path.append(node._coordinate)
            if node != self.begin_node and node != self.end_node:
                node._occupied = True
        #print(self.path._path)
    
    def reset_costs(self, open_nodes, closed_nodes):
        for node in open_nodes:
            node._f_cost = None
            node._h_cost = None
            node._g_cost = None
            node._parent = None
        for node in closed_nodes:
            node._f_cost = None
            node._h_cost = None
            node._g_cost = None
            node._parent = None

    def calculate_f_cost(self, node):
        """calculate f_cost of begin-node"""
        node._g_cost = manhattan_distince(self.begin_node, node)
        node._h_cost = manhattan_distince(node, self.end_node)
        node._f_cost = node._g_cost + node._h_cost

    def remove_neighbours(self, path):
        for i in range(len(path)):
            if i != 0:
                path[i]._neighbours.remove(path[i-1])
            if i != len(path)-1:
                path[i]._neighbours.remove(path[i+1])
