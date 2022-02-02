from importlib.resources import open_binary
import classes.board as brd
from code.functions.functions import get_distance, manhattan_distance
from queue import Empty, PriorityQueue

class Heap: 
    ''' Object capable of being retrieved from heap. '''
    def __init__(self, f_cost, h_cost, node):
        self.f_cost = f_cost
        self.h_cost = h_cost
        self.node = node

    def __lt__(self,other):
        ''' Sort prioritylist by f-cost and h-cost. '''
        if self.f_cost == other.f_cost:    
            return self.h_cost < other.h_cost
        return self.f_cost < other.f_cost   


class A_star:
    """ A* path-finding algorithm. """
    def __init__(self, path):
        self.path = path
        self.begin_node = self.path._net_gates[0]
        self.end_node = self.path._net_gates[1]
    
    def run_a_star(self):
        ''' Run A* pathfinding algorithm. '''
        open_nodes = PriorityQueue()
        closed_nodes = set()
        self.calculate_f_cost(self.begin_node)

        # put data object into the priority-queue
        open_nodes.put(Heap(self.begin_node._f_cost, self.begin_node._h_cost, self.begin_node))

        while open_nodes:

            if not open_nodes.queue:
                return

            current_node = open_nodes.get(0).node
            closed_nodes.add(current_node)

            # in case the end-node has been reached
            if current_node == self.end_node:
                path_nodes = self.retrace_path()
                self.remove_neighbours(path_nodes)
                self.set_as_occupied(path_nodes)
                self.reset_costs(open_nodes, closed_nodes)
                return
            
            # check if neighbours are traversable
            for neighbour in current_node._neighbours:
                if neighbour in closed_nodes or (neighbour.has_gate() and neighbour != self.end_node and neighbour != self.begin_node):
                    continue
                
                # check whether new path to neighbour is shorter or if neighbour is not yet in the open-list
                movement_cost = current_node._g_cost + 1 + self.get_level_costs(neighbour)
                if neighbour._occupied:
                    # intersection-cost equals 300
                    movement_cost += 300
                if (neighbour._g_cost != None and movement_cost < neighbour._g_cost) or not self.check_open_nodes(neighbour, open_nodes):
                    neighbour._g_cost = movement_cost
                    neighbour._h_cost = manhattan_distance(neighbour, self.end_node)
                    neighbour._f_cost = neighbour._g_cost + neighbour._h_cost
                    neighbour._parent = current_node
                    
                    # if neighbour not in open-list, add it
                    if not self.check_open_nodes(neighbour, open_nodes):

                        open_nodes.put(Heap(neighbour._f_cost, neighbour._h_cost, neighbour))

    def get_level_costs(self, node):
        ''' Add costs for lower grid-levels. '''
        height = node._coordinate[2]
        # height_cost = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}
        height_cost = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 0, 6: 0, 7: 0, 8: 0}

        cost = height_cost[height]
        return cost

    def check_open_nodes(self, neighbour, open_nodes):
        ''' Check whether node is already in open-nodes. '''
        for items in open_nodes.queue:
            if items.node == neighbour:
                return True
        return False

    def retrace_path(self):
        ''' Starting with end-node, retrace path back to begin. '''
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
        """ Set all the nodes in list as occupied for next paths and put coordinates of nodes in the path-net. """
        for node in path_nodes:
            self.path._path.append(node._coordinate)
            if node != self.begin_node and node != self.end_node:
                node._occupied = True
    
    def reset_costs(self, open_nodes, closed_nodes):
        ''' Set all A* costs back to normal value for next paths. '''
        for node in open_nodes.queue:
            node.node._f_cost = None
            node.node._h_cost = None
            node.node._g_cost = None
            node.node._parent = None
        for node in closed_nodes:
            node._f_cost = None
            node._h_cost = None
            node._g_cost = None
            node._parent = None

    def calculate_f_cost(self, node):
        """calculate f_cost of begin-node"""
        node._g_cost = manhattan_distance(self.begin_node, node)
        node._h_cost = manhattan_distance(node, self.end_node)
        node._f_cost = node._g_cost + node._h_cost

    def remove_neighbours(self, path):
        ''' Remove neighbours, making double laid paths impossible. '''
        for i in range(len(path)):
            if i != 0:
                path[i]._neighbours.remove(path[i-1])
            if i != len(path)-1:
                path[i]._neighbours.remove(path[i+1])