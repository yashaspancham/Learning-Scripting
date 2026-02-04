import time
count=1

while True:
    time.sleep(1)
    print(count)
    if count>=5:
        print("Limit reached, exiting")
        break
    count+=1


