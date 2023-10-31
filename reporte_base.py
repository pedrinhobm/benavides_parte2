import csv
import random

# Crear una lista de pacientes aleatorios
data = []
for paciente_id in range(1, 11):
    edad = random.randint(18, 80)  # Edad aleatoria entre 18 y 80 años
    diagnostico = random.choice([0, 1])  # Diagnóstico aleatorio (0 o 1)
    data.append([paciente_id, edad, diagnostico])

# Escribir los datos en un archivo CSV
with open("pacientes.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["paciente", "edad", "diagnóstico"])  # Encabezados
    csvwriter.writerows(data)

print("Archivo 'pacientes.csv' creado con éxito.")
