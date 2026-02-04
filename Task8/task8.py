items=["apple","bannana","cherry","date","elderberry"]

for item in items:
    with open("data.txt","a") as f:
        f.write(item+"\n")

with open("data.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        if "bannana" in line:
            with open("result.txt","a") as res:
                res.write(line)
