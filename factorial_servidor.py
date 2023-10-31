import socket

# Función para calcular el factorial
def factorial(x):
    if x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

# Configurar el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)

print("Esperando conexiones...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión desde {addr}")

    # Recibir el número entero desde el cliente
    num = int(client_socket.recv(1024).decode())

    # Calcular el factorial
    fact = factorial(num)

    # Enviar el resultado al cliente
    client_socket.send(str(fact).encode())

    client_socket.close()
