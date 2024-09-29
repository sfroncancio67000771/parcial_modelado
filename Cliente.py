import zmq
import time

def cliente():
    contexto = zmq.Context()
    socket = contexto.socket(zmq.DEALER)  # Cada cliente tiene un DEALER para identificarse
    identidad = f"cliente-{time.time()}"  # Identidad única del cliente
    socket.setsockopt_string(zmq.IDENTITY, identidad)
    socket.connect("tcp://localhost:5555")  # Conectar al servidor

    while True:
        mensaje = input("Introduce el mensaje (o 'todos' para enviar a todos): ")
        
        if mensaje == 'todos':
            socket.send_string("Mensaje a todos los nodos")
        else:
            socket.send_string(mensaje)

        respuesta = socket.recv_multipart()
        print(f"Respuesta del servidor: {respuesta}")

# Ejecutar cliente
cliente()
