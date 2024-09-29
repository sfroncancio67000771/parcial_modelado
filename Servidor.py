import zmq
import threading
import time

# Lista de nodos conectados (IPs de clientes)
nodos_conectados = []

# Función para manejar las conexiones y mensajes
def servidor():
    contexto = zmq.Context()
    socket = contexto.socket(zmq.ROUTER)  # Usamos ROUTER para poder identificar a los nodos
    socket.bind("tcp://*:5555")  # Escuchar en todos los IPs en el puerto 5555

    while True:
        identidad, mensaje = socket.recv_multipart()
        mensaje_decodificado = mensaje.decode('utf-8')
        
        if identidad not in nodos_conectados:
            nodos_conectados.append(identidad)

        print(f"Mensaje recibido de {identidad.decode()}: {mensaje_decodificado}")

        # Responder con lista de nodos conectados
        socket.send_multipart([identidad, b'Lista de nodos:'] + nodos_conectados)

# Hilo para ejecutar el servidor
servidor_thread = threading.Thread(target=servidor)
servidor_thread.start()
