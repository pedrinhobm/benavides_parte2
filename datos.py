# En el cliente
numero_entero = 42
client_socket.send(str(numero_entero).encode())

# En el servidor
numero_recibido = int(client_socket.recv(1024).decode())

-----------------------------------------------------------
# Solicitar al usuario que ingrese un número entero
num = int(input("Ingrese un número entero: "))
# Enviar el número al servidor
client_socket.send(str(num).encode())

# Recibir el número entero desde el cliente
num = int(client_socket.recv(1024).decode())
# Calcular el factorial
fact = factorial(num)
# Enviar el resultado al cliente
client_socket.send(str(fact).encode())

# Recibir el resultado del servidor
resultado = client_socket.recv(1024).decode()
------------------------------------------------------------

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

----------------------------------------------------------------------------------
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
_____________________________________________________________________________________________
    # Agregar la información a la base de datos (archivo CSV)
    with open('pacientes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        paciente_info = data.split(',')
        writer.writerow(paciente_info)
------------------------------------------------------------------------------------------------------

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





# Leer las notas desde un archivo CSV y convertirlas a enteros
def leer_notas():
    with open("notas.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        notas = next(reader)
    return [int(nota) for nota in notas]

# Leer y enviar las notas al servidor
notas = leer_notas()
client_socket.send(",".join(map(str, notas)).encode())

# Recibir las notas desde el cliente
notas_str = client_socket.recv(1024).decode()
notas = [int(nota) for nota in notas_str.split(",")]

# envia
 _, _, pacientes_sanos = calcular_estadisticas()
client_socket.send(str(pacientes_sanos).encode())
# recive
resultado = client_socket.recv(1024).decode()
print("Resultado:", resultado)


# Solicitar estadísticas al servidor
opcion = input("Seleccione una opción (a, b, o c): ")
client_socket.send(opcion.encode())

opcion = client_socket.recv(1).decode()
