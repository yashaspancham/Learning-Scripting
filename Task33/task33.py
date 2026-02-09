#ShortCut Soltuion
# import subprocess
# subprocess.run(["find","-name","*.log","-mtime","+7","-delete"])

#Proper Solution
import os
import time

files=os.listdir("./temp_logs/")
log_files=[]
for file in files:
    if file.endswith(".log"):
        log_files.append(file)
current_time = time.time()

for log_file in log_files:
    file_age= (current_time - os.path.getmtime(f"./temp_logs/{log_file}"))
    if file_age > 7*24*60*60:
        os.remove(f"./temp_logs/{log_file}")
        print(f"Removing file name: {log_file}, age: {file_age}")
