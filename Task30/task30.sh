#!/bin/bash
set -u

trap "echo 'Cleanup in progress... Goodbye!'; exit 0" SIGINT    

while true; do
    echo "Working..."
    sleep 1
done