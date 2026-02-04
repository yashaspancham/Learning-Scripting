FILENAME='config.txt'

if [[ -f $FILENAME ]]; then
    echo "File found, proceeding..."
else
    echo "Error: File missing"
fi 
