# file_info=$( ls -l | grep "audit_log.txt" )
# file_permissions=${file_info:1:3}

# if [[ $file_permissions == *w*  ]]; then
if [[ -w audit_log.txt ]]; then
    echo "File is writable"
    else
    chmod 600 audit_log.txt
    echo "Read and write permission added"
fi
