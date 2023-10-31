import socket
import csv

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)

    while True:
        print("Esperando cliente...")
        client, addr = server.accept()
        print(f"Conexión establecida con {addr}")
        receive_data(client)

def receive_data(client):
    data = client.recv(1024).decode()
    client.close()

    # Agregar la información a la base de datos (archivo CSV)
    with open('pacientes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        paciente_info = data.split(',')
        writer.writerow(paciente_info)
        
    print("Datos recibidos del cliente:")
    print(data)
    print("Paciente registrado con éxito.")

if __name__ == '__main__':
    main()
