import subprocess
import os
import getpass

currD = os.path.dirname(os.path.abspath("MyShell.py"))
shellD = os.path.dirname(os.path.abspath(__file__))

while True:
    print(currD + ">>>", end="")
    command = input()
    if command == "exit":
        break
    elif command == "hello":
        print("hello " + getpass.getuser())
    elif command.startswith("cd"):
        path = command.split(" ")[1]

        try:
            os.chdir(path)
            currD = os.getcwd()
        except Exception as e:
            print("The system cannot find the path specified.")

    elif command.startswith("ls"):
        parts = command.split(" ", 1)
        file_to_ls = currD
        if len(parts) > 1:
            file_to_ls = parts[1]
        subprocess.run([os.path.join(shellD, "ls.bat"),file_to_ls])

    elif command.startswith("hexdump"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            file_to_hexdump = parts[1]
            subprocess.run([os.path.join(shellD, "hexdump.bat"),file_to_hexdump])

    elif command.startswith("grep"):
        parts = command.split(" ", 2)
        if len(parts) == 3:
            subprocess.run([os.path.join(shellD, "grep.bat"), parts[1], parts[2]])
            print()
