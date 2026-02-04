#!/bin/bash
set -u

backup_paths=(
  "/etc/passwd"
  "/etc/shadow"
  "/etc/group"
  "/etc/gshadow"
  "/etc/sudoers"
  "/etc/hostname"
  "/etc/hosts"
  "/etc/resolv.conf"
  "/etc/fstab"
  "/etc/crontab"
)


timestamp_adder(){
    local file="$1"
    local timestamp=$(date "+%Y%m%d_%H%M")
    local new_filename="${file}_${timestamp}.bak"
    echo "$new_filename"
}

mkdir -p backups
touch "missing_files.log"
echo "Missing files in etc during backup process" >> "missing_files.log"

echo "Stating backup process..."

for file in "${backup_paths[@]}";do
    filename=$(basename "$file")
    new_filename=$(timestamp_adder "$filename")
    if [ -f "$file" ]; then
        cp "$file" "backups/$new_filename"
    else
        echo "$file" >> "missing_files.log"
    fi 
done

echo "Backup process completed."