( cd /tmp/no_folder ) > /dev/null 2>&1

if [[ $? -eq 0 ]]; then
    echo "Success"
    exit 0
else
    exit 1
fi