import socket
import json
import time
import numpy as np

PORTA_TX_PARA_CANAL = 9001
PORTA_CANAL_PARA_RX = 9002


def aplicar_ruido(sinal, media=0.0, desvio_padrao=0.0):
    if desvio_padrao == 0:
        return sinal
    sinal_array = np.array(sinal, dtype=float)
    ruido = np.random.normal(media, desvio_padrao, size=sinal_array.shape)
    sinal_com_ruido = sinal_array + ruido
    return sinal_com_ruido.tolist()


def _log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] [CANAL] {msg}")


def iniciar_canal(media=0.0, desvio_padrao=0.0, callback_etapas=None):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('localhost', PORTA_TX_PARA_CANAL))
    servidor.listen(1)
    _log(f"servidor TCP escutando na porta {PORTA_TX_PARA_CANAL} (aguardando TX)")

    conn, addr = servidor.accept()
    _log(f"conexao aceita do TX: {addr}")

    dados = b''
    while True:
        parte = conn.recv(65536)
        if not parte:
            break
        dados += parte
    conn.close()
    servidor.close()
    _log(f"recebidos {len(dados)} bytes do TX, conexao fechada")

    sinal_limpo = json.loads(dados.decode('utf-8'))
    sinal_ruidoso = aplicar_ruido(sinal_limpo, media, desvio_padrao)
    _log(f"ruido aplicado: x={media}, sigma={desvio_padrao}")

    if callback_etapas:
        callback_etapas({
            'sinal_limpo': sinal_limpo,
            'sinal_ruidoso': sinal_ruidoso,
            'media': media,
            'desvio_padrao': desvio_padrao,
        })

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', PORTA_CANAL_PARA_RX))
    _log(f"conectado ao RX na porta {PORTA_CANAL_PARA_RX}, enviando sinal ruidoso")