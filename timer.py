import subprocess
import time

start = time.time()
n_runs = 0

i = 250
while time.time() - start < 3600:
    subprocess.call(["python3", "main_hill.py", "1", "6", f"{i}", "20"])
    i = i + 250
    n_runs += 1
