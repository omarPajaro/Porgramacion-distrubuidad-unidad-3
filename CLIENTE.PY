import socket

mi_socket = socket.socket()

mi_socket.connect(("localhost", 8000))

print("Conectado al servidor.")

while True:
    message = input("Tú: ")
    mi_socket.send(message.encode('utf-8'))
