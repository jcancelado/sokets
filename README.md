# Chat Bidireccional con Sockets en Python

Este proyecto implementa un sistema de chat en tiempo real utilizando sockets y hilos en Python. Permite que múltiples clientes se conecten a un servidor central y se comuniquen entre sí simultáneamente.

## Características

* **Arquitectura Cliente-Servidor:** Un servidor central gestiona las conexiones.
* <img width="796" height="48" alt="image" src="https://github.com/user-attachments/assets/224503ff-9155-43aa-bbe8-f2e79d904159" />

* **Comunicación Bidireccional:** Uso de hilos (`threading`) para enviar y recibir mensajes al mismo tiempo sin bloqueos.
* <img width="612" height="117" alt="image" src="https://github.com/user-attachments/assets/ccec55d4-8210-4d43-a29e-f13f57aab22f" />

* **Broadcasting:** Los mensajes enviados por un usuario son visibles para todos los demás conectados. Ejemplo de como se ve desde el celular
<img width="1073" height="758" alt="image" src="https://github.com/user-attachments/assets/64fe5aa2-a9ca-4f1f-be5c-4ef39a87aa39" />

# Codigo

## servidor.py
<img width="379" height="601" alt="image" src="https://github.com/user-attachments/assets/0a5ac1ec-726d-4f74-a5c1-f1adab0d4fef" />

## cliente.py
<img width="340" height="432" alt="image" src="https://github.com/user-attachments/assets/c45b7f0c-e069-4d19-8692-efad78ea1a7b" />



## Requisitos

* Python 3.x instalado.

## Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/jcancelado/sokets.git
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

* **Librería `socket` (La Conexión)**
  Se utiliza para crear el puente de comunicación entre los equipos (cliente y servidor), asegurando que los mensajes lleguen completos y en el orden correcto.

* **Librería `threading` (Multitarea)**
  Permite realizar varias acciones al mismo tiempo para que el chat sea fluido:
  * **En el Servidor:** Crea un proceso independiente por cada usuario, lo que permite atender a todos los compañeros simultáneamente sin esperas.
  * **En el Cliente:** Separa la recepción y el envío de mensajes. Esto permite que puedas leer lo que te escriben tus compañeros justo mientras estás redactando tu propio mensaje, sin que la pantalla se congele.
