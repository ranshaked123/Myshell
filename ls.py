import sys
import os
directory = sys.argv[1]
if os.path.isdir(directory):
    print("Directory: " + directory)
    for item in os.listdir(directory):
            print(item)
else:
    print("doesnt exist")