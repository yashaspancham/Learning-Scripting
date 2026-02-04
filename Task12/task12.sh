count=0

logs=( "error" "warning" "error" "success" "error" )

for log in "${logs[@]}"; do
    if [[ $log == "error" ]]; then
        ((count++))
    fi
done

echo "Total Errors: $count"