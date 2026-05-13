import socket
import threading
from transmissor import iniciar_tx
from receptor import iniciar_rx

def simular(texto, callback):
    sock_tx, sock_rx = socket.socketpair()
    
    thread_tx = threading.Thread(target=iniciar_tx, args=(sock_tx, texto))
    thread_rx = threading.Thread(target=iniciar_rx, args=(sock_rx, callback))
    
    thread_tx.start()
    thread_rx.start()