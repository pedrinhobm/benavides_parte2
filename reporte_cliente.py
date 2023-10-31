import socket
import csv

# Configurar el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

# Solicitar estadísticas al servidor
opcion = input("Seleccione una opción (a, b, o c): ")
client_socket.send(opcion.encode())

# Recibir y mostrar los resultados
resultado = client_socket.recv(1024).decode()
print("Resultado:", resultado)

# Cerrar la conexión del cliente después de obtener los resultados
client_socket.close()
