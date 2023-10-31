import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12346))
    server.listen(1)
    client_conn = None

    while True:
        if client_conn is None:
            print("Esperando cliente para enviar conteo...")
            client_conn, client_addr = server.accept()
            print(f"Conexión establecida con {client_addr}")
        data = client.recv(1024).decode()
        byte_count = len(data)
        print(f">>HOLA SOY SERVIDOR Y HE RECIBIDO DE MASTER {byte_count} bytes:")
        print(f'"{data}"')
        send_count(client_conn, byte_count)

def send_count(client_conn, byte_count):
    client_conn.send(str(byte_count).encode())

if __name__ == '__main__':
    main()