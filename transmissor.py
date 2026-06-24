import json
from registro import MODULACOES, ENQUADRAMENTOS, DETECCAO_CORRECAO
from utils import text_to_bits

def iniciar_tx(sock, texto, mod, enq, edc, callback_etapas=None):
    codificar_mod, _ = MODULACOES[mod]
    enquadrar, _ = ENQUADRAMENTOS[enq]
    add_edc, _ = DETECCAO_CORRECAO[edc]

    bits = text_to_bits(texto)
    bits_com_edc = add_edc(bits)
    quadro = enquadrar(bits_com_edc)
    sinal = codificar_mod(quadro)

    etapas = {
        'texto_original': texto,
        'bits': bits,
        'bits_com_edc': bits_com_edc,
        'quadro': quadro,
        'sinal': sinal,
    }

    if callback_etapas:
        callback_etapas(etapas)

    dados = json.dumps(sinal).encode('utf-8')
    sock.sendall(dados)
    sock.close()