import random as rd
from queue import PriorityQueue
import copy

from classes.board import Board
from a_star import A_star
from netlist_functions import random_netlist, swap_netlist

class HillClimber:
    """
    Hill climber changes netlist order for a* algorithm until a lowest cost is reached.
    Repeats multiple times.
    """

    def __init__(self, net_list, gate_list):
        self.net_list_original = net_list
        self.gate_list = gate_list

    def run(self, restarts, max_reverts):
        hill_list = []
        best_netlists = PriorityQueue()

        self.restarts = restarts
        self.max_reverts = max_reverts

        for i in range(self.restarts):

            self.net_list = copy.deepcopy(self.net_list_original)

            self.repeats = 0
            self.revert_counter = 0

            board = Board(self.gate_list, self.net_list)

            while True:

                # create board for current net list
                board = Board(self.gate_list, self.net_list)

                # add nets to the path-objects
                for path in board._paths:
                    a_star = A_star(path)
                    a_star.run_a_star()

                # calculate and display costs
                costs = board.calculate_costs()
                print(f"{i}.{self.repeats}", end="")
                print(f"\tcost = {costs[0]}")
                print(f"\tintersections = {costs[1]}")
                print(f"\tgate intersections = {costs[2]}")
                print(f"\ttotal = {costs[3]}")
                print()

                # save netlist if new total cost is lower, always save first run
                if self.compare_costs(costs[3]) == True:
                    saved_net_list = copy.deepcopy(self.net_list)

                    print('SAVING!')
                    print()
                
                # revert to saved netlist if total cost is higher
                else:
                    self.net_list = copy.deepcopy(saved_net_list)
                    print('REVERTING!')
                    print()
                
                if self.end_loop() == False:
                    self.net_list = self.net_swap(self.net_list)
                    
                    hill_list.append(self.lowest_costs)

                # run board and algorithm again for best outcome
                else:
                    board = Board(self.gate_list, self.net_list)

                    for path in board._paths:
                        a_star = A_star(path)
                        a_star.run_a_star()

                    costs = board.calculate_costs()

                    print()
                    print("BEST CONFIG:")
                    print(f"cost = {costs[0]}")
                    print(f"intersections = {costs[1]}")
                    print(f"gate intersections = {costs[2]}")
                    print(f"total = {costs[3]}")
                    print()

                    hill_list.append(self.lowest_costs)

                    break

            best_netlists.put((costs[3], self.net_list))

        optimal_config = best_netlists.get()

        # run board and algorithm for best outcome overall
        board = Board(self.gate_list, optimal_config[1])

        for path in board._paths:
            a_star = A_star(path)
            a_star.run_a_star()

        costs = board.calculate_costs()

        print()
        print("BEST OVERALL CONFIG:")
        print(f"cost = {costs[0]}")
        print(f"intersections = {costs[1]}")
        print(f"gate intersections = {costs[2]}")
        print(f"total = {costs[3]}")
        print()

        return (board, costs, hill_list)

    def run_new(self, restarts, max_reverts):

        dict_of_used_netlist= {}
        self.restarts = restarts
        self.max_reverts = max_reverts

        for i in range(restarts):
            net_file_list = copy.deepcopy(self.net_list_original)
            random_start_netlist = random_netlist(net_file_list)

            if str(random_start_netlist) in dict_of_used_netlist.keys():
                random_start_netlist = random_netlist(net_file_list)
            
            self.repeats = 0
            self.revert_counter = 0

            # create board for current net list
            board = Board(self.gate_list, random_start_netlist)

            # add nets to the path-objects
            for path in board._paths:
                a_star = A_star(path)
                a_star.run_a_star()

            # calculate and display costs
            costs = board.calculate_costs()

            print(f"{i}.{self.repeats}", end="")
            print(f"\tcost = {costs[0]}")
            print(f"\tintersections = {costs[1]}")
            print(f"\ttotal = {costs[2]}")
            print()

            # append netlists and total costs to dictonary
            dict_of_used_netlist[str(random_start_netlist)] = costs[2]

        print()
        # sorteds the dictonary by total costs 
        sorted_netlist = sorted(dict_of_used_netlist, key=dict_of_used_netlist.get) 


        for i in range(max_reverts):
            for i in range(len(sorted_netlist[:5])):

                # makes 1 swap in the top best netlist
                list_of = eval(sorted_netlist[i]) 
                mutation = swap_netlist(list_of)

                # create board for current net list
                board = Board(self.gate_list, mutation)

                # add nets to the path-objects
                for path in board._paths:
                    a_star = A_star(path)
                    a_star.run_a_star()

                # calculate and display costs
                costs = board.calculate_costs()

                print(f"{i}.{self.repeats}", end="")
                print(f"\tcost = {costs[0]}")
                print(f"\tintersections = {costs[1]}")
                print(f"\ttotal = {costs[2]}")
                print()
                dict_of_used_netlist[str(mutation)]=costs[2]

        sorted_netlist = sorted(dict_of_used_netlist, key=dict_of_used_netlist.get) 
        print(f"end_dict = {dict_of_used_netlist}")
        print()
        print("BEST CONFIG:")
        print(f"net_list = {sorted_netlist[0]}")
        best_board = Board(self.gate_list, eval(sorted_netlist[0]))

        for path in best_board._paths:
            a_star = A_star(path)
            a_star.run_a_star()
        best_costs = best_board.calculate_costs()

        print(f"cost = {best_costs[0]}")
        print(f"intersections = {best_costs[1]}")
        print(f"total = {best_costs[2]}")
        print()
        return (best_board, best_costs, best_costs)

    def compare_costs(self, costs):
        if self.repeats == 0 or costs < self.lowest_costs:
            self.lowest_costs = costs
            self.repeats += 1
            self.revert_counter = 0

            return True

        self.repeats += 1
        self.revert_counter += 1

        return False

    def net_swap(self, net_list):       
        random_element = rd.randrange(1, len(net_list))
        net_list[random_element], net_list[0] = net_list[0], net_list[random_element]

        return net_list

    def end_loop(self):
        if self.revert_counter == self.max_reverts:
            return True

        return False