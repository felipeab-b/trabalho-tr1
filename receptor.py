import json
from registro import MODULACOES, ENQUADRAMENTOS, DETECCAO_CORRECAO
from utils import bits_to_text

TAMANHO_EDC = {
    'paridade': 1,
    'checksum': 8,
    'crc': 32,
}

def iniciar_rx(sock, mod, enq, edc, callback):
    _, decodificar_mod = MODULACOES[mod]
    _, desenquadrar = ENQUADRAMENTOS[enq]
    _, verify_edc = DETECCAO_CORRECAO[edc]

    dados = sock.recv(65536)
    sinal = json.loads(dados.decode('utf-8'))

    quadro = decodificar_mod(sinal)
    if isinstance(quadro, list):
        quadro = ''.join(quadro)
    bits_com_edc = desenquadrar(quadro)
    edc_ok = verify_edc(bits_com_edc)

    tamanho_edc = TAMANHO_EDC[edc]
    bits = bits_com_edc[:-tamanho_edc]

    texto = bits_to_text(bits)
    callback(texto, sinal, edc_ok)
    sock.close()