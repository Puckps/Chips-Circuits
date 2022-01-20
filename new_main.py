from functions import plot_graph, plot_2d
from sys import argv
import pandas as pd
from classes.board import Board
from greedy import Greedy


if len(argv) != 3:
    print("Usage: python3 filename main [chip nr] [netist file nr]")
gate_file = f"data/gates&netlists/chip_{argv[1]}/print_{argv[1]}.csv"
net_file = f"data/gates&netlists/chip_{argv[1]}/netlist_{argv[2]}.csv"

board = Board(gate_file, net_file)

net_list = []
path_list = []
length = 0

# add nets to the path-objects
for path in board._paths:
    #net = path.shortest_path()
    greedy = Greedy(path)
    greedy.run_greedy()
    print(path._path)
    net = path._path
    path_str = str(net).replace(" ", "")
    net_output = f"({int(path._net_gates[0].get_gate().id)},{int(path._net_gates[1].get_gate().id)})"
    net_list.append(net_output)
    path_list.append(path_str)
    #length = length + len(path._path)
#length = length - len(path_list)

df = pd.DataFrame({"net": net_list, "wires": path_list})
df2 = {"net": f"chip_{argv[1]}_net_{argv[2]}", "wires" : board.calculate_costs()}
df = df.append(df2, ignore_index=True)
df.to_csv("output.csv", index=False)

plot_graph(board._nodes, board._paths, board._dimensions[0], board._dimensions[1])
plot_2d(board._nodes, board._paths, board._dimensions[0], board._dimensions[1])