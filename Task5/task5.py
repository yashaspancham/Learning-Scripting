import os

for i in range(1,6):
    open(f"file{i}.txt","a").close()

for i in os.listdir("."):
    if i.endswith(".txt"):
        if "3" in i:
            print(f"Found the special file: {i}")
        else:
            print(f"Checking: {i}")