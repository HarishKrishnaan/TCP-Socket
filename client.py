
import threading
import time
import random

import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 30124
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    print(cs.recv(100).decode('utf-8'))

    # create message to send to server
    with open("in-proj.txt", 'r') as file:
        msg = file.readlines()
    
    outputFile = open("out-proj.txt", 'w')
    for line in msg:
        line = line.replace('\n', '').replace('\r', '')
        cs.sendall(line.encode('utf-8'))
        data_from_server=cs.recv(100)
        outputFile.write((data_from_server.decode('utf-8') + "\n"))
    
    endMessage = "end"

    cs.sendall(endMessage.encode('utf-8'))
    cs.close()


if __name__ == "__main__":
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    print("Done.")