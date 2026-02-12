#!/bin/bash

id -u developer > /dev/null 2>&1 

if [[ $? -eq 0 ]]; then
    echo "User found."
else
    echo "User missing - please create it."
fi