SCORE=7
GUESS=0

GUESS=int(input("Guess a number between 1 and 10: "))

while GUESS != SCORE:
    GUESS=int(input("Guess again: "))

print("YOu have guessed the correct number!!")
