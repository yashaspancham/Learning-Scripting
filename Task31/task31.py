import subprocess

flag=subprocess.run(
    ["ping","-c","1","www.google.com"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
    )

if flag.returncode==0:
    print("Network is UP")
else:
    print("Network is DOWN")