#!/bin/bash

disk_info=$( df -h / | awk 'NR==2 {print $5}'  )
disk_percentage=$( echo "$disk_info" | tr -d '%' )

if [[ $disk_percentage -gt 90 ]]; then
    echo "Low Disk Space!"
else
    echo "Disk Space OK."
fi