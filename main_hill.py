from functions import plot_graph, plot_2d, plot_hill_graph
from sys import argv
import pandas as pd

from load import import_gates, import_net
from hill_climber import HillClimber

from netlist_functions import *


if len(argv) != 5:
    print("Usage: python3 filename main [chip nr] [netist file nr] [nr of restarts] [nr of reverts before restart]")

gate_file = f"data/gates&netlists/chip_{argv[1]}/print_{argv[1]}.csv"
net_file = f"data/gates&netlists/chip_{argv[1]}/netlist_{argv[2]}.csv"
gate_list = import_gates(gate_file)
net_list = import_net(net_file)

restarts = int(argv[3])
max_reverts = int(argv[4])

# pick netlist transformation

# reverse_netlist(net_list)
# random_netlist(net_list)
# net_list = copy.deepcopy(most_used_gate(net_list))
# net_list = copy.deepcopy(least_used_gate(net_list))

HC = HillClimber(net_list, gate_list)
results = HC.run_new(restarts, max_reverts)

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

# generate output file
df = pd.DataFrame({"net": net_list, "wires": path_list})
df2 = {"net": f"chip_{argv[1]}_net_{argv[2]}", "wires" : costs[2]}
df = df.append(df2, ignore_index=True)
df.to_csv("output.csv", index=False)

# plot graphs
plot_graph(board._nodes, board._paths, board._dimensions[0], board._dimensions[1])
plot_2d(board._nodes, board._paths, board._dimensions[0], board._dimensions[1])
plot_hill_graph(hill_list)