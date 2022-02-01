import subprocess
import time

start = time.time()
n_runs = 0

i = 500
while time.time() - start < 7200:
    subprocess.call(["python3", "main_hill.py", "1", "6", f"{i}", "20"])
    i = i + 500
    n_runs += 1
