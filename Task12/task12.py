count = 0
logs = ["error", "waring","error","success","error"]

for log in logs:
    if log == "error":
        count+=1


print(f"Total Erros: {count}")