#!/bin/bash

#will use https://mock.httpstatus.io/mocking-data
#end url with /error-code to get that error-code

urls=("https://mock.httpstatus.io/404" "https://mock.httpstatus.io/200" "https://mock.httpstatus.io/204")

health_check() {
    url=$1
    http_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [[ $? -eq 0 ]]; then
        if [[ $http_code -eq 200 ]]; then
            echo "$url -> Website is Live."
        else
            echo "$url -> Website Error: $http_code"
        fi
    else
        echo "$url -> Website to down"
    fi
}

for url in "${urls[@]}"; do
    health_check "$url"
done