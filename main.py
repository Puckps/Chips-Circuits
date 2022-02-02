from sys import argv
import pandas as pd


from code.algoritme.greedy import Greedy
from code.algoritme.a_star_priority import A_star
from code.algoritme.hill_climber import HillClimber
from classes.path import Path


from code.functions.functions import plot_graph
from code.functions.load import import_gates, import_net
from code.functions.netlist_functions import *



# ------------------------------------ Greedy ------------------------------------
# from code.algoritme.greedy import Greedy
# from classes.board import Board

# if len(argv) != 3:
#     print("Usage: python3 filename main [chip nr] [netist file nr]")

# gate_file = f"data/gates&netlists/chip_{argv[1]}/print_{argv[1]}.csv"
# net_file = f"data/gates&netlists/chip_{argv[1]}/netlist_{argv[2]}.csv"
# gate_list = import_gates(gate_file)
# net_list = import_net(net_file)

# board = Board(gate_list, net_list)
# net_list = []
# path_list = []
# length = 0

# # add nets to the path-objects
# for path in board._paths:
#     greedy = Greedy(path)
#     greedy.run_greedy()

#     net = path._path
#     path_str = str(net).replace(" ", "")
#     net_output = f"({int(path._net_gates[0].get_gate().id)},{int(path._net_gates[1].get_gate().id)})"
#     net_list.append(net_output)
#     path_list.append(path_str)

# costs = board.calculate_costs()

# print()
# print("BEST CONFIG:")
# print(f"cost = {costs[0]}")
# print(f"intersections = {costs[1]}")
# print(f"total = {costs[2]}")
# print()




# ------------------------------------ A* ------------------------------------
# from a_star_priority import A_star
# from classes.board import Board

# if len(argv) != 3:
#     print("Usage: python3 filename main [chip nr] [netist file nr]")

# gate_file = f"data/gates&netlists/chip_{argv[1]}/print_{argv[1]}.csv"
# net_file = f"data/gates&netlists/chip_{argv[1]}/netlist_{argv[2]}.csv"
# gate_list = import_gates(gate_file)
# net_list = import_net(net_file)

# board = Board(gate_list, net_list)
# net_list = []
# path_list = []
# length = 0

# # add nets to the path-objects
# for path in board._paths:
#     a_star = A_star(path)
#     a_star.run_a_star()

#     net = path._path
#     path_str = str(net).replace(" ", "")
#     net_output = f"({int(path._net_gates[0].get_gate().id)},{int(path._net_gates[1].get_gate().id)})"
#     net_list.append(net_output)
#     path_list.append(path_str)

# costs = board.calculate_costs()

# print()
# print("BEST CONFIG:")
# print(f"cost = {costs[0]}")
# print(f"intersections = {costs[1]}")
# print(f"total = {costs[2]}")
# print()




# ------------------------------------ Hill Climber ------------------------------------


if len(argv) != 5:
    print("Usage: python3 filename main [chip nr] [netist file nr] [nr of restarts] [nr of reverts before restart]")

gate_file = f"data/gates&netlists/chip_{argv[1]}/print_{argv[1]}.csv"
net_file = f"data/gates&netlists/chip_{argv[1]}/netlist_{argv[2]}.csv"
gate_list = import_gates(gate_file)
net_list = import_net(net_file)

restarts = int(argv[3])
max_reverts = int(argv[4])

HC = HillClimber(net_list, gate_list)
results = HC.run(restarts, max_reverts)

board = results[0]
costs = results[1]
hill_list = results[2]

# get stats for model and output file
net_list = []
path_list = []

for path in board._paths:
    net = path._path
    path_str = str(net).replace(" ", "")
    net_output = f"({int(path._net_gates[0].get_gate().id)},{int(path._net_gates[1].get_gate().id)})"
    net_list.append(net_output)
    path_list.append(path_str)

best_df = pd.DataFrame({"netlist": [hill_list],"score": [costs[2]], "intersections": [costs[1]], "restarts": [argv[3]], "max_reverts": [argv[4]]})

with open(f"output/chip_{argv[1]}/output_netlist_{argv[2]}.csv", 'a') as f:
    best_df.to_csv(f, header=False, index=False)



# ------------------------------------ Output ------------------------------------

df = pd.DataFrame({"net": net_list, "wires": path_list})
df2 = {"net": f"chip_{argv[1]}_net_{argv[2]}", "wires" : costs[2]}
df = df.append(df2, ignore_index=True)
df.to_csv("output/output.csv", index=False)

plot_graph(board._nodes, board._paths, board._dimensions[0], board._dimensions[1])

