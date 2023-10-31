import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12346))

    while True:
        count = client.recv(1024).decode()
        print(f">>HOLA SOY CLIENTE Y LA CANTIDAD DE CARACTERES RECIBIDA POR SERVIDOR ES: {count}")

if __name__ == '__main__':
    main()
