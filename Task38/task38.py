import psutil

print(f"System has {psutil.cpu_count()} and {psutil.virtual_memory().total/(1024*1024):.2f} MB")