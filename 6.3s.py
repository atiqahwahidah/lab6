import socket
import sys
import time
import errno
from multiprocessing import Process
import math

init_message = ('ONLINE CALCULATOR\n\n1. Log\n2. Square Root\n3. Exponential\n4. Power\n5. Exit\nPlease choose: ')

def log():
    s_sock.send(str.encode('Enter number[log]:'))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    s_sock.send(str.encode('Enter base:'))
    base = s_sock.recv(2048)
    base = base.decode('utf-8')
    base = int(base)
    print(f'base is {base}')
    res = math.log(x, base)
    print(f'The result is {res}')
    s_sock.sendall(str.encode(f'Result: {res}'))

def sqrt():
    s_sock.send(str.encode('Enter number[square root]: '))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    res = math.sqrt(x)
    print(f'The result is {res}')
    s_sock.sendall(str.encode(f'Result: {res}'))

def exp():
    s_sock.send(str.encode('Enter power[exponent]: '))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    res = math.exp(x)
    print(f'The result is {res}')
    s_sock.sendall(str.encode(f'Result: {res}'))

def pow():
    s_sock.send(str.encode('Enter number[power]: '))
    x = s_sock.recv(2048)
    x = x.decode('utf-8')
    x = int(x)
    print(f'x is {x}')
    s_sock.send(str.encode('Enter power: '))
    powe = s_sock.recv(2048)
    powe = powe.decode('utf-8')
    powe = int(powe)
    print(f'power is {powe}')
    res = math.pow(x, powe)
    print(f'The result is {res}')
    s_sock.sendall(str.encode(f'Result: {res}'))

def process_start(s_sock):
    s_sock.send(str.encode('Welcome!\n\n1. Log\n2. Square Root\n3. Exponential\n4. Power\n5. Exit\nChoose what you want: '))
    while True:
        enc_data = s_sock.recv(2048)
        data = enc_data.decode('utf-8')
        print(data)
        if not data:
            break
        if data == '1':
            log()
        elif data == '2':
            sqrt()
        elif data == '3':
            exp()
        elif data == '4':
            pow()
        elif data == '5':
            break
        else:
            continue
        s_sock.sendall(str.encode(init_message))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                print('Connected...')
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:
                print('got a socket error...')

    except Exception as e:
        print('an exception occurred!')
        print(e)
       	sys.exit(1)
    finally:
     	   s.close()
