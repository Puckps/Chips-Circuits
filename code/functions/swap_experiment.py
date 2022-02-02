import subprocess
# In experiment 1, we have tested what the effect is of the amount of swaps one makes in the hillclimber
# In the experiments there were 3 conditions: 1 swap, 5 swaps and 10 swaps
# All the conditions were called 10 times on chip 1 with netlist 5, with max 30 reverts and 30 restarts
# In order to run the experiments, change the value of the 'swap' variable in hillclimber.py

n_runs = 0

while n_runs < 10:
    subprocess.call(["python3", "main.py", "1", "5", "30", "30"])
    n_runs += 1