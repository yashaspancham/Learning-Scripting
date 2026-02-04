TEMP=14

if [ $TEMP -gt 30 ]; then 
    echo "Hot"
elif [[ $TEMP -ge 15  &&  $TEMP -le 30 ]]; then
    echo "Warm"
else
    echo "Cold"
fi