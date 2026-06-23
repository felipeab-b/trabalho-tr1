import json
from registro import MODULACOES, ENQUADRAMENTOS, DETECCAO_CORRECAO
from utils import text_to_bits

def iniciar_tx(sock, texto, mod, enq, edc):
    codificar_mod, _ = MODULACOES[mod]
    enquadrar, _ = ENQUADRAMENTOS[enq]
    add_edc, _ = DETECCAO_CORRECAO[edc]

    bits = text_to_bits(texto)
    bits_com_edc = add_edc(bits)       
    quadro = enquadrar(bits_com_edc)
    sinal = codificar_mod(quadro)

    dados = json.dumps(sinal).encode('utf-8')
    sock.sendall(dados)
    sock.close()