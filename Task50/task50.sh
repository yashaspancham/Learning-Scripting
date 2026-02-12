#!/bin/bash

#we will send data to www.webhook.site 

cpu=$(nproc)

process_ok=true
ps -e | grep "python3" > /dev/null 2>&1
if [[ $? -ne 0 ]]; then
    process_ok=false
fi

web_ok=true
ping -c 1 www.google.com > /dev/null 2>&1
if [[ $? -ne 0 ]]; then
    web_ok=false
fi

mem=$(free -h | awk "NR==2 {print \$2 }")

data=$(jq -n \
    --arg mem "$mem"\
    --argjson cpu "$cpu"\
    --argjson process_ok "$process_ok"\
    --argjson web_ok "$web_ok"\
    '{host:"prod", cpu: $cpu, mem: $mem, process_ok: $process_ok, web_ok: $web_ok}'
)


curl -X POST \
    -H 'Content-Type: application/json' \
    -d "$data" \
    "$HOOK_URL"