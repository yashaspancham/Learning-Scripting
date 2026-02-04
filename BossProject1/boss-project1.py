data = ["INFO: Start", "ERROR: Connection failed", "INFO: Retrying", "ERROR: Timeout"]
counter=0
new_data=[]

for entry in data:
    if "ERROR: " in entry:
        counter+=1
        new_entry = entry.replace("ERROR","FIXED")
        new_data.append(new_entry)
    else:
        new_data.append(entry)


print(f"Errors: {counter}")

print(new_data)