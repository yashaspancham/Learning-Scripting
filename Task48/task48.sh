#!/bin/bash

#we will be uisng https://webhook.site/ 

JSON_data(){
    hostname="prod-web-01"
    cpu_usage=45
    status="healthy"

    jq -n --arg host "$hostname" --argjson cpu "$cpu_usage" --arg status "$status" \
     '{host:$host , cpu: $cpu, status: $status}'
}

data=$(JSON_data)


curl -X POST -H "Content-Type: application/json" \
    -d "$data" \
    https://webhook.site/6b5c8d27-f704-4b0d-8801-1b2338650171