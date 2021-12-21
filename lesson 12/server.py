import socket


clients = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 9090))

print('Start server')

while True:
      data, addres = server_socket.recvfrom(1024)

      if addres not in clients:
         clients.append(addres)

      print(addres[0], addres[1], data.decode('utf-8'))

      for client in clients:
         if addres != client:
            server_socket.sendto(data, client)

server_socket.close()