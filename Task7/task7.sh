check_status(){
    local number=$1
    echo "Checking status for number: $number" #not present in gemini task 
    if [ $number -gt 50 ]; then
        echo "Status: High"
    else
        echo "Status: Low"
    fi
}

check_status 30
check_status 60
check_status 50
check_status 100