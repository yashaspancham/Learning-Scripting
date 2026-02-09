#!/bin/bash

cpu_cores=$(nproc)

total_memory=$(free -m | awk "NR==2 {print \$2 }")

echo "System has $cpu_cores and $total_memory MB of RAM"