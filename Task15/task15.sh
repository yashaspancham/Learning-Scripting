count=1

while true; do
    sleep 1
    echo $count
    if [ $count -eq 5 ];then
        echo "Limit reached, exiting"
        break
    fi
    (( count++ ))
done