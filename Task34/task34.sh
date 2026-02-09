#!/bin/bash

( pgrep python3 ) >/dev/null 2>&1

if [[ $? -eq 0 ]]; then
    echo "Process is healthy"
else
    echo "CRITICAL: Process not found"
fi