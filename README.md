# Chat Bidireccional con Sockets en Python

Este proyecto implementa un sistema de chat en tiempo real utilizando sockets TCP/IP y threading en Python. Permite que múltiples clientes se conecten a un servidor central y se comuniquen entre sí simultáneamente.

## Características

* **Arquitectura Cliente-Servidor:** Un servidor central gestiona las conexiones.
* **Comunicación Bidireccional:** Uso de hilos (`threading`) para enviar y recibir mensajes al mismo tiempo sin bloqueos.
* **Broadcasting:** Los mensajes enviados por un usuario son visibles para todos los demás conectados.

## Requisitos

* Python 3.x instalado.

## Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone <URL_DE_TU_REPO>
    cd chat-bidireccional-sockets
    ```

2.  **Iniciar el Servidor:**
    Abre una terminal y ejecuta:
    ```bash
    python server.py
    ```
    *Verás un mensaje indicando que el servidor está escuchando.*

3.  **Iniciar los Clientes:**
    Abre tantas terminales nuevas como usuarios desees simular y en cada una ejecuta:
    ```bash
    python client.py
    ```

4.  **Chatear:**
    * Ingresa un "nickname" cuando se te solicite.
    * Escribe mensajes y presiona Enter. Verás cómo aparecen en las ventanas de los otros clientes.

## Explicación Técnica

* **Librería `socket`**: Se utiliza `AF_INET` (IPv4) y `SOCK_STREAM` (TCP) para garantizar la entrega de paquetes.
* **Librería `threading`**:
    * En el **Servidor**: Se crea un hilo por cada cliente conectado para manejar sus mensajes de forma aislada.
    * En el **Cliente**: Se separan las funciones de `recibir` (escuchar) y `escribir` (enviar) en hilos distintos para que el input del usuario no bloquee la recepción de mensajes.