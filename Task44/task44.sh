#!/bin/bash

http_code=$(curl -s -o /dev/null -w '%{http_code}' http://13.232.3.65/)

if [[ $? -eq 0 ]]; then
    if [[ $http_code -eq 200 ]]; then
        echo "Website is Live."
    else
        echo "Website Error: $http_code"
    fi
else
    echo "Website is down"
fi
