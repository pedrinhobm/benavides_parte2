import csv
import socket

# Función para calcular estadísticas
def calcular_estadisticas():
    with open("pacientes.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Saltar la primera fila de encabezados
        edades = []
        pacientes_enfermos = 0
        pacientes_sanos = 0

        for row in csvreader:
            _, edad, diagnostico = map(int, row)
            edades.append(edad)
            if diagnostico == 0:
                pacientes_sanos += 1
            elif diagnostico == 1:
                pacientes_enfermos += 1

        promedio_edades = sum(edades) / len(edades)
        return promedio_edades, pacientes_enfermos, pacientes_sanos

# Configurar el servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(5)  # Aceptar hasta 5 conexiones simultáneas

print("Esperando conexiones...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión desde {addr}")
    
    opcion = client_socket.recv(1).decode()
    if opcion == "a":
        promedio_edades, _, _ = calcular_estadisticas()
        client_socket.send(str(promedio_edades).encode())
    elif opcion == "b":
        _, pacientes_enfermos, _ = calcular_estadisticas()
        client_socket.send(str(pacientes_enfermos).encode())
    elif opcion == "c":
        _, _, pacientes_sanos = calcular_estadisticas()
        client_socket.send(str(pacientes_sanos).encode())
    else:
        client_socket.send("Opción no válida".encode())

    client_socket.close()

