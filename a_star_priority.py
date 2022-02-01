from importlib.resources import open_binary
import classes.board as brd
from functions import get_distance, manhattan_distince
from queue import Empty, PriorityQueue

class Data: 

    def __init__(self,score1,score2,node, id):
        self.f_cost=score1
        self.h_cost=score2
        self.node=node
        self.id = id

    def __repr__(self): # print function
        return f"f-cost:{self.f_cost} h-cost:{self.h_cost} node:{self.node}"

    def __lt__(self,other): # for PriorityQueue, compare less-then self with other
        if self.f_cost==other.f_cost:    
            return self.h_cost<other.h_cost
        return self.f_cost<other.f_cost   

    # def hash_string(self): # for set
    #     return f"{self.x} {self.y} {self.z}" # this is the string to store/look-up the data with

class A_star:
    """
    A* algorithm
    """
    def __init__(self, path):
        self.path = path
        self.begin_node = self.path._net_gates[0]
        self.end_node = self.path._net_gates[1]
    
    
    def run_a_star(self):
        open_nodes = PriorityQueue()
        closed_nodes = set()
        self.calculate_f_cost(self.begin_node)
        # put data object into the priority-queue
        id = 0
        open_nodes.put(Data(self.begin_node._f_cost, self.begin_node._h_cost, self.begin_node, id))

        while open_nodes:

            if len(open_nodes.queue) == 0:
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
                NewMovementCostToNeighbour = current_node._g_cost + 1 + self.check_z_value(neighbour)                      #manhattan_distince(current_node, neighbour)
                if neighbour._occupied == True:
                    NewMovementCostToNeighbour += 300
                if (neighbour._g_cost != None and NewMovementCostToNeighbour < neighbour._g_cost) or self.check_open_nodes(neighbour, open_nodes) == False: #neighbour not in open_nodes:
                    neighbour._g_cost = NewMovementCostToNeighbour
                    neighbour._h_cost = manhattan_distince(neighbour, self.end_node)
                    neighbour._f_cost = neighbour._g_cost + neighbour._h_cost
                    neighbour._parent = current_node
                    
                    # if neighbour not in open-list, add it
                    if self.check_open_nodes(neighbour, open_nodes) == False: #neighbour not in open_nodes:
                        id += 1
                        open_nodes.put(Data(neighbour._f_cost, neighbour._h_cost, neighbour, id))
                        #open_nodes.append(neighbour)

    def check_z_value(self, node):
        height = node._coordinate[2]
        height_cost = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}
        # height_cost = {0: 8, 1: 7, 2: 6, 3: 5, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

        cost = height_cost[height]
        return cost

    def check_open_nodes(self, neighbour, open_nodes):
        for items in open_nodes.queue:
            if items.node == neighbour:
                return True
        return False

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
        node._g_cost = manhattan_distince(self.begin_node, node)
        node._h_cost = manhattan_distince(node, self.end_node)
        node._f_cost = node._g_cost + node._h_cost

    def remove_neighbours(self, path):
        for i in range(len(path)):
            if i != 0:
                path[i]._neighbours.remove(path[i-1])
            if i != len(path)-1:
                path[i]._neighbours.remove(path[i+1])