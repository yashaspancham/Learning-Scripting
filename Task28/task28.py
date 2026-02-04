import os
import sys

try:
    os.chdir("/temp/no_folder")
    print("Success")
    sys.exit(0) 
except Exception as e:
    sys.exit(1)