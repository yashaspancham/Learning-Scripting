import subprocess


try:
    subprocess.run([
        "ssh", "-i" ,"delete_later_ec2.pem" ,
   "-o", "ConnectTimeout=10",
   "-o", "BatchMode=yes",
    "-o", "StrictHostKeyChecking=no",
   "-o", "UserKnownHostsFile=/dev/null",
   "ec2-user@3.108.53.182", "tar -xf /tmp/backup.tar.gz -C /tmp/"
    ],
    timeout=20,
    check=True)
    print("Extraction successful.")
except subprocess.TimeoutExpired:
    print("Connection Timedout")
except Exception as e:
    print("Error: ",e)