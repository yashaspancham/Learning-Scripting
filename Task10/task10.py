import sys
import os

if os.path.exists("config.txt"):
    sys.exit(0)
else:
    sys.exit(1)