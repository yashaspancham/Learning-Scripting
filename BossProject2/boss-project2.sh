check_status() {
    if [[ $1 -ge 90 ]] ; then
        return 1
    else
        return 0
    fi
}

cpu_percentage=( 20 75 95 )

for cpu in "${cpu_percentage[@]}" ; do
    check_status $cpu
    status=$?
    if [[ $status -eq 1 ]] ; then  
        echo "Alert: Shutdown initiated!"
        break
    fi
done