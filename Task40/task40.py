import subprocess

pwd_info=subprocess.check_output(["chage","-l","developer"])

pwd_info=pwd_info.decode()

print((pwd_info.split("\n")[0]).split(":")[1])