flag=$1

case "$flag" in 
    --start)
        echo "System starting..."
        ;;
    --stop)
        echo "System stopping..."
        ;;
    *)
        echo "Invalid option"
        ;;
esac