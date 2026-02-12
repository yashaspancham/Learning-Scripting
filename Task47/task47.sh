#!/bin/bash

hostname="prod-web-01"
cpu_usage=45
status="healthy"

jq -n --arg host "$hostname" --argjson cpu "$cpu_usage" --arg status "$status" \
 '{host:$host , cpu: $cpu, status: $status}'