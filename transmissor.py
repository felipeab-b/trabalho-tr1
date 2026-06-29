import json
import socket
from registro import MODULACOES_BANDA_BASE, MODULACOES_PORTADORA, ENQUADRAMENTOS, DETECCAO_CORRECAO
from utils import text_to_bits
from canal import PORTA_TX_PARA_CANAL


def iniciar_tx(texto, mod_base, mod_portadora, enq, edc, callback_etapas=None):
    codificar_base, _ = MODULACOES_BANDA_BASE[mod_base]
    codificar_portadora, _ = MODULACOES_PORTADORA[mod_portadora]
    enquadrar, _ = ENQUADRAMENTOS[enq]
    add_edc, _, _ = DETECCAO_CORRECAO[edc]

    bits = text_to_bits(texto)
    bits_com_edc = add_edc(bits)
    quadro = enquadrar(bits_com_edc)
    sinal_base = codificar_base(quadro)
    sinal = codificar_portadora(sinal_base)

    etapas = {
        'texto_original': texto,
        'bits': bits,
        'bits_com_edc': bits_com_edc,
        'quadro': quadro,
        'sinal_base': sinal_base,
        'sinal': sinal,
    }

    if callback_etapas:
        callback_etapas(etapas)

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', PORTA_TX_PARA_CANAL))
    cliente.sendall(json.dumps(sinal).encode('utf-8'))
    cliente.close()