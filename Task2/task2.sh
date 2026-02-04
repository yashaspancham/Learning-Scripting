SCORE=85
GRADE=""

if [ $SCORE -ge 90 ]; then
    GRADE="A"
elif [ $SCORE -ge 80 ] && [ $SCORE -le 89 ] ; then
    GRADE="B"
elif [ $SCORE -ge 70 ] && [ $SCORE -le 79 ] ; then
    GRADE="C"
else 
    GRADE="F"
fi

echo "$GRADE"