import subprocess

try:
    subprocess.run(
        [
            "scp", "-i", "delete_later_ec2.pem",
            "-o", "BatchMode=yes",
            "-o", "ConnectTimeout=20",
            "-o", "StrictHostKeyChecking=no",
            "-o", "UserKnownHostsFile=/dev/null",
            "backup.tar.gz",
            "ec2-user@3.7.55.8:/tmp/"
        ],
        timeout=30,
        check=True
    )
except subprocess.TimeoutExpired:
    print("SCP timedout")
except Exception as e:
    print("Error: ",e)
