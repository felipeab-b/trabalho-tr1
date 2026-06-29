import json
import socket
import time
from registro import MODULACOES_BANDA_BASE, MODULACOES_PORTADORA, DETECCAO_CORRECAO
from camada_enlace.enquadramento.fragmentacao import (
    desenquadrar_multiplo_contagem,
    desenquadrar_multiplo_flag_bytes,
    desenquadrar_multiplo_flag_bits,
)
from utils import bits_to_text
from canal import PORTA_CANAL_PARA_RX

DESENQUADRADORES_MULTIPLOS = {
    'nenhum': lambda bits: bits,
    'contagem': desenquadrar_multiplo_contagem,
    'flag_bytes': desenquadrar_multiplo_flag_bytes,
    'flag_bits': desenquadrar_multiplo_flag_bits,
}

TAMANHO_EDC = {
    'paridade': 8,
    'checksum': 8,
    'crc': 32,
}


def _log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] [RX] {msg}")


def iniciar_rx(mod_base, mod_portadora, enq, edc, callback):
    _, decodificar_base = MODULACOES_BANDA_BASE[mod_base]
    _, decodificar_portadora = MODULACOES_PORTADORA[mod_portadora]
    desenquadrar_multiplo = DESENQUADRADORES_MULTIPLOS[enq]
    _, verify_edc, tipo_edc = DETECCAO_CORRECAO[edc]

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('localhost', PORTA_CANAL_PARA_RX))
    servidor.listen(1)
    _log(f"servidor TCP escutando na porta {PORTA_CANAL_PARA_RX} (aguardando Canal)")

    conn, addr = servidor.accept()
    _log(f"conexao aceita do Canal: {addr}")

    dados = b''
    while True:
        parte = conn.recv(65536)
        if not parte:
            break
        dados += parte
    conn.close()
    servidor.close()
    _log(f"recebidos {len(dados)} bytes do Canal, conexao fechada")

    sinal_recebido = json.loads(dados.decode('utf-8'))

    sinal_base_recuperado = decodificar_portadora(sinal_recebido)
    quadro_demodulado = decodificar_base(sinal_base_recuperado)
    if isinstance(quadro_demodulado, list):
        quadro_demodulado = ''.join(quadro_demodulado)

    bits_com_edc = desenquadrar_multiplo(quadro_demodulado)

    if tipo_edc == 'correcao':
        bits_finais = verify_edc(bits_com_edc)
        edc_ok = True
    else:
        edc_ok = verify_edc(bits_com_edc)
        bits_finais = bits_com_edc[:-TAMANHO_EDC[edc]]

    texto_final = bits_to_text(bits_finais)
    _log(f"texto recuperado: {texto_final!r} (edc_ok={edc_ok})")

    etapas = {
        'sinal_recebido': sinal_recebido,
        'sinal_base_recuperado': sinal_base_recuperado,
        'quadro_demodulado': quadro_demodulado,
        'bits_com_edc': bits_com_edc,
        'edc_ok': edc_ok,
        'bits_finais': bits_finais,
        'texto_final': texto_final,
    }

    callback(etapas)