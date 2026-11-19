import sys

if len(sys.argv) == 3:
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        print("File does not exist")
        exit()
    word = sys.argv[2]
else:
    file = sys.stdin
    word = sys.argv[1]

i = 1
for line in file:
    if word in line:
        print(i, line, end="")
    i += 1

if file != sys.stdin:
    file.close()