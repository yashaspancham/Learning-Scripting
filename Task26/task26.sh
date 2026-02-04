#!/bin/bash

current_date=$(date "+%Y%m%d_%H%M")


tar -czvf "etc_backups_[$current_date].tar.gz" "backups"  

rm -rf backups