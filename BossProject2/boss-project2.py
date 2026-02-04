def check_status(cpu_leve:int):
    if cpu_leve >90:
        return 1
    else:
        return 0

cpu_percentage=[20,75,95]

for cpu in cpu_percentage:
    status=check_status(cpu)
    if status==1:
        print(f"Alert: Shutdown initiated!")
        break