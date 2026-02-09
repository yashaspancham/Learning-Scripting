import os

script_pid=os.getpid()

all_processes=os.popen("ps -e")
output_string=all_processes.read()
output=output_string.split("\n")

for process in output:
    if "python3" in process and str(script_pid) not in process:
        print("Process is healthy")
        exit(0)

print("CRITICAL: Process not found")


