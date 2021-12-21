import socket
import threading
import json
import time
from log import log

@log
def json_convert(name, message, time):    
    base = {'name' : name,
    'message' : message,
    'time' : time}
    return json.dumps(base)
    

def read_message(sock):
    while True:
        data, addres = sock.recvfrom(1024)        
        base = data.decode('utf-8')
        base = json.loads(base)
        name = base['name']
        message = base['message']
        print(f"[{name}]: {message}")        


def get_message(sock, name):
    while True:
        message = input('[You]: ')
        timest = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime())

        born_json = json_convert(name, message, timest)

        if message != "":
            sock.sendto(born_json.encode('utf-8'), server)
        
server = ('localhost', 9090)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect(('localhost', 9090))

name = input('Name: ')

rT = threading.Thread(target=read_message, args=(client_socket, ))
gT = threading.Thread(target=get_message, args=(client_socket, name))

rT.start()
gT.start()

rT.join()
gT.join()

client_socket.close()