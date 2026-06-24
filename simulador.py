# simulador.py
import socket
import threading
from transmissor import iniciar_tx
from receptor import iniciar_rx

def simular(texto, mod, enq, edc, callback, callback_etapas_tx=None):
    sock_tx, sock_rx = socket.socketpair()

    thread_tx = threading.Thread(
        target=iniciar_tx,
        args=(sock_tx, texto, mod, enq, edc, callback_etapas_tx)
    )
    thread_rx = threading.Thread(
        target=iniciar_rx,
        args=(sock_rx, mod, enq, edc, callback)
    )

    thread_tx.start()
    thread_rx.start()