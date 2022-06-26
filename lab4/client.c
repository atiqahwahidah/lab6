#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>

int main(int argc, char *argv[])
{
int socket_desc;
struct sockaddr_in server;
char *message, server_reply[2000];

socket_desc=socket(AF_INET,SOCK_STREAM,0);
if(socket_desc==-1)
{
printf("Socket cannot be created!");
}

server.sin_addr.s_addr=inet_addr("192.168.56.103");
server.sin_family=AF_INET;
server.sin_port=htons(22);

if(connect(socket_desc,(struct sockaddr *)&server, sizeof(server))<0)
{
puts("Connect ERROR");
return 1;
}

puts("Connected\n");
message="connect";

if(send(socket_desc,message,strlen(message),0)<0)
{
puts("Send FAILED!");
return 1;
}
puts("Data Send\n");

if(recv(socket_desc,server_reply,2000,0)<0)
{
puts("recv FAILED");
}
puts("Reply received\n");
puts(server_reply);
return 0;
}
