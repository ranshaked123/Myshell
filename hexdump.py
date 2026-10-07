import sys
import os
import binascii

file_path = sys.argv[1]

if os.path.isfile(file_path):
    with open(file_path, "rb") as file:
        data = file.read()

    for i in range(0, len(data), 16):
        chunk = data[i:i + 16]
        hex_part = binascii.hexlify(chunk).decode()
        print(hex_part)

else:
    print("File does not exist")

