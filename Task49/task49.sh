#!/bin/bash

if [[ -z "$API_KEY" ]]; then
    echo "Error: API_KEY environment variable not set!"
else
    echo "API Key found: ${API_KEY:0:4}****"
fi