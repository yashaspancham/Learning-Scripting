def check_status(number:int) -> None:
    print(f"Checking status for number: {number}") #not present in gemini task
    if number >50:
        print("Status: High")
    else:
        print("Status: Low")


check_status(75)
check_status(30)
check_status(50)
check_status(100)