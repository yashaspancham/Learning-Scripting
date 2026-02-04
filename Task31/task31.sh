#!/bin/bash

ping -c 1 "www.google.com" > /dev/null 2>&1

ping_flag=$?

if [[ $ping_flag -eq 0 ]]; then
    echo "Network is UP"
else
    echo "Network is DOWN"
fi