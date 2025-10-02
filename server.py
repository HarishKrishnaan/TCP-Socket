import threading
import time
import random

import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('0.0.0.0', 30124)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    continueLoop = True
    while(continueLoop):
        data_from_server=csockid.recv(100).decode('utf-8')
        msg = data_from_server.swapcase()[::-1]
        if (msg == "DNE"):
            break
        csockid.send(msg.encode('utf-8'))


    ss.close()
    exit()



if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    print("Done.")
