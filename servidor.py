import socket
import threading

# Configuración del servidor
HOST = '0.0.0.0'  # Localhost
PORT = 55555        # Puerto arbitrario (no reservado)

# Inicializar socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    """Envía un mensaje a todos los clientes conectados."""
    for client in clients:
        client.send(message)

def handle(client):
    """Maneja la conexión individual de un cliente."""
    while True:
        try:
            # Recibir mensaje del cliente
            message = client.recv(1024)
            broadcast(message)
        except:
            # Si falla (ej. cliente se desconecta), cerrar conexión
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} salió del chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    """Función principal para aceptar conexiones."""
    print(f"Servidor escuchando en {HOST}:{PORT}...")
    while True:
        client, address = server.accept()
        print(f"Conectado con {str(address)}")

        # Solicitar nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname del cliente es {nickname}")
        broadcast(f"{nickname} se unió al chat!".encode('utf-8'))
        client.send('Conectado al servidor!'.encode('utf-8'))

        # Iniciar hilo para manejar al cliente
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()