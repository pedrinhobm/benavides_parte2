import socket
import csv

# Leer las notas desde un archivo CSV y convertirlas a enteros
def leer_notas():
    with open("notas.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        notas = next(reader)
    return [int(nota) for nota in notas]

# Calcular el promedio final
def calcular_promedio(notas):
    Pa = (sum(notas[0:4]) - min(notas[0:4])) / 3
    laboratorios = sorted(notas[4:14])
    Pb = (sum(laboratorios[2:]) / 8)
    Ta = notas[14]
    NF = (3 * Pa + 3 * Pb + 4 * Ta) / 10
    return NF

# Configurar el cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345))

# Leer y enviar las notas al servidor
notas = leer_notas()
client_socket.send(",".join(map(str, notas)).encode())

# Recibir y mostrar el promedio final
promedio_final = float(client_socket.recv(1024).decode())
print(f"El promedio final es: {promedio_final}")

client_socket.close()

