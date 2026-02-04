SCORE=85
GRADE=""

if SCORE >= 90:
    GRADE = "A"
elif SCORE >=80 and SCORE <=89:
    GRADE = "B"
elif SCORE >=70 and SCORE <= 79:
    GRADE = "C"
else :
    GRADE = "F"

print(GRADE)