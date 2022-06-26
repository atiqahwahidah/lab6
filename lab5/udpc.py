import socket

msgClient= "Client here!"
bytesToSend= str.encode(msgClient)
serverPort= ("192.168.56.103", 20001)
buffer= 1024

UDPC_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPC_sock.sendto(bytesToSend, serverPort)

msgServer = UDPC_sock.recvfrom(buffer)

msg = "{}".format(msgServer[0])
print(msg)
