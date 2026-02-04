data=( "INDO: Start" "ERROR: Connection failed" "INFO: Retrying" "ERROR: Timeout" )
new_array=()
counter=0
for entry in "${data[@]}"; do
    if [[ $entry == ERROR:* ]];then
        ((counter++))
        new_entry=$( echo "$entry" | sed 's/ERROR/FIXED/' )
        new_array+=("$new_entry")
    else
        new_array+=( "$entry" )
    fi
done

echo "Errors: $counter"
for entry in "${new_array[@]}";do
    echo "$entry"
done