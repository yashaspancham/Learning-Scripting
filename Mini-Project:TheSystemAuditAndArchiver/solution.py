from datetime import datetime
import os
import shutil

backup_paths = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/group",
    "/etc/gshadow",
    "/etc/sudoers",
    "/etc/hostname",
    "/etc/hosts",
    "/etc/resolv.conf",
    "/etc/fstab",
    "/etc/crontab",
]


def filename_with_timestamp(base_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    new_filename= f"{base_name}_{timestamp}.bak"
    return new_filename

os.makedirs("backups", exist_ok=True)

with open("missing_files.log","w") as log_file:
    log_file.write("Missing files of etc during backup process.")

print("Starting backup process...")

for path in backup_paths:
    basename=os.path.basename(path)
    new_filename=filename_with_timestamp(basename)
    if os.path.isfile(path):
        shutil.copy2(path,f"backups/{new_filename}")
    else:
        with open("missing_files.log","a") as log_file:
            log_file.write(f"{path}\n")

print("Backup process completed.")