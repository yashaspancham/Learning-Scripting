input="The server is DOWN"

ouput=$(echo $input | sed "s/DOWN/UP/")

echo $ouput