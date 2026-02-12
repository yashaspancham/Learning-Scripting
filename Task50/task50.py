import os
import subprocess
import requests
import psutil

def bytes_to_Gib(b):
    return str(round(b / (1024 ** 3), 2))+"Gi"

#we will send data to www.webhook.site 

cpu_cores=os.cpu_count()

service_health=False
script_pid=os.getpid()
all_process=subprocess.check_output(["ps","-e"]).decode()
process=all_process.split("\n")
for proc in process:
    if "python3" in proc and str(script_pid) not in proc:
        service_health=True
        break


mem=bytes_to_Gib(psutil.virtual_memory().total) 

connected=False
try:
    ping_output=subprocess.check_output(["ping", "-c", "1", "www.google.com"])
    connected=True
except Exception as e:
    print(f"Error: {e}")

data={
    "host":"prod",
    "cpu":cpu_cores,
    "mem":mem,
    "process_ok":service_health,
    "web_ok":connected
    }

url=os.environ.get("HOOK_URL")

try:
    requests.post(url, json=data,timeout=5)
except Exception as e:
    print(f"Error: {e}")