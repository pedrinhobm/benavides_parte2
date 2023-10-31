import socket

# Configurar el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

# Solicitar al usuario que ingrese un número entero
num = int(input("Ingrese un número entero: "))

# Enviar el número al servidor
client_socket.send(str(num).encode())

# Recibir el resultado del servidor
resultado = client_socket.recv(1024).decode()
print(f"El factorial de {num} es: {resultado}")

client_socket.close()
