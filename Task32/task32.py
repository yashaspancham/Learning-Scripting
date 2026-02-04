import shutil

disk_usage=shutil.disk_usage("/")
disk_used=float(disk_usage[1])
disk_total=float(disk_usage[0])
disk_free=float(disk_usage[2])
disk_used_percentage=((disk_used/disk_total)*100)

if disk_used_percentage>=90:
    print("Low Disk Space!")
else:
    print("Disk Space OK.")
