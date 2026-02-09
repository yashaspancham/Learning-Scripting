import os

script_pid=os.getpid()

isServiceRunning=False

every_process=os.popen('ps -e').read()
for process in every_process.split("\n"):
    if "python3" in process and str(script_pid) not in process:
        isServiceRunning=True
        break

if isServiceRunning:
    print("Service is up")
else:
    print("Service down! Restarting...")
    os.popen("python3 webapp.py > service.log 2>&1 &")