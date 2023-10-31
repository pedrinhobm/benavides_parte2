import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    nombre = input("Ingrese datos del paciente\nNombre(s): ")
    apellidos = input("Apellidos: ")
    peso = input("Peso(kg): ")
    talla = input("Talla(cm): ")
    edad = input("Edad: ")
    seguro = input("¿Cuenta con seguro? (s/n): ")

    # Envía la información al servidor
    data = f"{nombre},{apellidos},{peso},{talla},{edad},{seguro}"
    client.send(data.encode())
    print("Enviando al servidor...")

if __name__ == '__main__':
    main()
