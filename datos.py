# En el cliente
numero_entero = 42
client_socket.send(str(numero_entero).encode())

# En el servidor
numero_recibido = int(client_socket.recv(1024).decode())


# En el cliente
numero_decimal = 3.14159
client_socket.send(str(numero_decimal).encode())

# En el servidor
numero_decimal_recibido = float(client_socket.recv(1024).decode())


# En el cliente
lista_numeros = [1, 2, 3, 4, 5]
datos = ",".join(map(str, lista_numeros)
client_socket.send(datos.encode())

# En el servidor
datos_recibidos = client_socket.recv(1024).decode()
lista_numeros_recibida = [int(x) for x in datos_recibidos.split(",")]


# En el cliente
letra = "A"
client_socket.send(letra.encode())

# En el servidor
letra_recibida = client_socket.recv(1024).decode()


# En el cliente
lista_letras = ["a", "b", "c", "d", "e"]
datos = "".join(lista_letras)
client_socket.send(datos.encode())

# En el servidor
datos_recibidos = client_socket.recv(1024).decode()
lista_letras_recibida = list(datos_recibidos)


# En el cliente
verso = "I'm a highway star\nNobody gonna take my car\nI'm gonna race it to the ground"
client_socket.send(verso.encode())

# En el servidor
verso_recibido = client_socket.recv(1024).decode()


# En el cliente
import json
mi_diccionario = {"nombre": "Juan", "edad": 30}
datos = json.dumps(mi_diccionario)
client_socket.send(datos.encode())


# En el servidor
import json
datos_recibidos = client_socket.recv(1024).decode()
diccionario_recibido = json.loads(datos_recibidos)


# En el cliente
from datetime import datetime
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
client_socket.send(fecha_hora.encode())

# En el servidor
from datetime import datetime
fecha_hora_recibida = client_socket.recv(1024).decode()
fecha_hora_objeto = datetime.strptime(fecha_hora_recibida, "%Y-%m-%d %H:%M:%S")


# Agregar información a la base de datos CSV:
import csv

# Datos que deseas agregar
nuevo_paciente = {"paciente": "11", "edad": 35, "diagnostico": 1}

# Nombre del archivo CSV
archivo_csv = "base_de_datos.csv"

# Abre el archivo CSV en modo escritura
with open(archivo_csv, mode='a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["paciente", "edad", "diagnostico"])
    
    # Escribe la nueva fila en el archivo CSV
    writer.writerow(nuevo_paciente)

# Recuperar información de la base de datos CSV:
import csv

# Nombre del archivo CSV
archivo_csv = "base_de_datos.csv"

# Abre el archivo CSV en modo lectura
with open(archivo_csv, mode='r') as file:
    reader = csv.DictReader(file)
    
    # Recorre las filas del archivo y muestra los datos
    for row in reader:
        print(f"Paciente: {row['paciente']}, Edad: {row['edad']}, Diagnóstico: {row['diagnostico']}")
