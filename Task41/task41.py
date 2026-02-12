import subprocess

try:
    subprocess.run(
        ["ssh", "-o", "ConnectTimeout=5", "-o", "BatchMode=yes", "user@3.7.55.8", "exit"],
        timeout=5,
    )
except Exception as e:
    print("Error: ",e)
