import subprocess
import os

currD = os.path.dirname(os.path.abspath("MyShell.py"))

while True:
    print(currD + ">>>", end="")
    command = input()
    if command == "exit":
        break
    elif command == "hello":
        print("hello")
    elif command.startswith("cd"):
        path = command.split(" ")[1]

        try:
            os.chdir(path)
            currD = os.getcwd()
        except Exception as e:
            print("The system cannot find the path specified.")

    elif command.startswith("ls"):
        parts = command.split(" ")
        file_to_ls = None
        if len(parts) > 1:
            file_to_ls = parts[1]
        subprocess.run(["ls.bat",file_to_ls])
