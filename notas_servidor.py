import socket

# Función para calcular el promedio final
def calcular_promedio_final(notas):
    Pa = (sum(notas[0:4]) - min(notas[0:4])) / 3
    laboratorios = sorted(notas[4:14])
    Pb = (sum(laboratorios[2:]) / 8)
    Ta = notas[14]
    NF = (3 * Pa + 3 * Pb + 4 * Ta) / 10
    return NF

# Configurar el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)

print("Esperando conexiones...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión desde {addr}")

    # Recibir las notas desde el cliente
    notas_str = client_socket.recv(1024).decode()
    notas = [int(nota) for nota in notas_str.split(",")]

    # Calcular el promedio final
    promedio_final = calcular_promedio_final(notas)

    # Enviar el promedio final al cliente
    client_socket.send(str(promedio_final).encode())

    client_socket.close()
