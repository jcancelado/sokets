import socket
import threading

# Elegir un apodo
nickname = input("Elige tu nickname: ")

# Conexión al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.100', 55555))

def receive():
    """Escucha mensajes del servidor constantemente."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ha ocurrido un error!")
            client.close()
            break

def write():
    """Envía mensajes al servidor."""
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Hilos para permitir bidireccionalidad simultánea
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()