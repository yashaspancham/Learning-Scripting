#!/bin/bash

if pgrep "python3" > /dev/null 2>&1; then
    echo "Service is up."
else
    echo "Service down!. Restarting..."
    python3 webapp.py > service.log 2>&1 & 
fi