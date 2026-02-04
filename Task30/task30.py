import time

try:
    while True:
        print("Working...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Cleanup in progress... Goodbye!")