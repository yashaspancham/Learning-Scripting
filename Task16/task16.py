import sys

flag = sys.argv[1]

match flag:
    case "--start":
        print("System starting...")
    case "--stop":
        print("System stopping...")
    case _:
        print("Invalid option")