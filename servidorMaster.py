import socket
import time

# Lee el archivo pregunta1.txt
with open('pregunta1.txt', 'r') as file:
    data = file.read()
    rows = data.split('\n')

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    client = None

    while True:
        if client is None:
            print("Esperando cliente...")
            client, addr = server.accept()
            print(f"Conexión establecida con {addr}")
        send_data(client)

def send_data(client):
    for row in rows:
        client.send(row.encode())
        time.sleep(1)

if __name__ == '__main__':
    main()
