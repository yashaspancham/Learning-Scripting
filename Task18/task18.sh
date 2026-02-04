( echo $((10/0)) ) 2>/dev/null 

if (( $? !=0 ));then
    echo "Division by zero error"
fi
