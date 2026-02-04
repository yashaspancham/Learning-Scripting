import os

FILENAME="config.txt"

if os.path.isfile(FILENAME):
    print("File found, proceeding...")
else:
    print("Error: File missing")
