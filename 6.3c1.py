import socket

ClientSocket = socket.socket()
host = '192.168.56.103'
port = 8888

print('Waiting connection...')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(2048)
print(Response.decode('utf-8'))
while True:
    Input = input('Choice: ')
    ClientSocket.send(str.encode(Input))
    if Input == '5':
        break
    if Input != '1' and Input != '2' and Input != '3' and Input != '4' and Input != '5':
        print('Enter valid input')
        continue    
    if Input == '1' or Input == '4':
        Response = ClientSocket.recv(2048)
        print(Response.decode('utf-8'))
        Input = input('Choice: ')
        ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))
    Input = input('Choice: ')
    ClientSocket.send(str.encode(Input))
    ans = ClientSocket.recv(2048)
    print(ans.decode('utf-8'))
    dud = input('\nPress any button to continue: ')
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))

ClientSocket.close()
