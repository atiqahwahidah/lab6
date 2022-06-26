import socket
import os
import subprocess

SEP = "<SEPERATE>"
BUFFER_SIZE = 4096
server_ip = "192.168.56.103"
port = 8008
while True:
    command = "ls"
    output = subprocess.run(command)
    print(output)
    filename = input("Enter file that you want to send:\n ")
    filesize = os.path.getsize(filename)
    con = input(f"File: {filename}\nConfirm (Y/N)?")
    if con == "Y" or con == "y":
        break;
s = socket.socket()
print(f"Connect with {server_ip}:{port}")
try:
    s.connect((server_ip,port))
    print("Connected.")
    print(f"Sending:\nFile: {filename}")
    s.send(f"{filename}".encode())
    print(f"Size: {filesize} bytes")
    s.send(f"{filesize}".encode())
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not (bytes_read):
                break
            s.sendall(bytes_read)
    print("Success!!")
except:
    print("FAIL TO CONNECT! PROGRAM IS TERMINATED!")
s.close()
