SCORE=7

echo "Guess a number between 1 and 10: "
read GUESS

while [ $GUESS -ne $SCORE ]; do
    echo "Guess again: "
    read GUESS
done

echo "You have guessed the correct number!!!"
