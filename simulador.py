import threading
import time
from transmissor import iniciar_tx
from receptor import iniciar_rx
from canal import iniciar_canal


def simular(texto, mod_base, mod_portadora, enq, edc, callback_rx,
            callback_etapas_tx=None, callback_etapas_canal=None,
            media_ruido=0.0, desvio_ruido=0.0):

    thread_rx = threading.Thread(
        target=iniciar_rx,
        args=(mod_base, mod_portadora, enq, edc, callback_rx)
    )
    thread_canal = threading.Thread(
        target=iniciar_canal,
        args=(media_ruido, desvio_ruido, callback_etapas_canal)
    )
    thread_tx = threading.Thread(
        target=iniciar_tx,
        args=(texto, mod_base, mod_portadora, enq, edc, callback_etapas_tx)
    )

    thread_rx.start()
    time.sleep(0.1)
    thread_canal.start()
    time.sleep(0.1)
    thread_tx.start()