import socket

mi_socket = socket.socket()

mi_socket.bind(("localhost", 8000))

mi_socket.listen(5)

clientes = []

print("Servidor iniciado. Esperando clientes...")

while True:
    conexion, addr = mi_socket.accept()
    print('Nueva conexión establecida desde:', addr)
    clientes.append(conexion)
    conexion.send(b"Bienvenido al chat. Ingresa 'exit' para salir.")

    while True:
        try:
            message = conexion.recv(1024).decode('utf-8')
            if message == 'exit':
                conexion.close()
                clientes.remove(conexion)
                break
            for cliente in clientes:
                if cliente != conexion:
                    cliente.send(message.encode('utf-8'))
        except Exception as e:
            print("Error:", e)
            conexion.close()
            clientes.remove(conexion)

