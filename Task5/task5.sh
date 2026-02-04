for i in {1..5}; do
    touch "file$i.txt"
done

for file in *.txt ; do
    if [[ $file == *3* ]]; then
        echo "Found the special file: $file"
    else 
        echo "Checking $file"
    fi
done