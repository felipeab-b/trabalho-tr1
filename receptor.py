import json
from registro import MODULACOES, ENQUADRAMENTOS, DETECCAO_CORRECAO
from utils import bits_to_text

TAMANHO_EDC = {
    'paridade': 8,
    'checksum': 8,
    'crc': 32,
}

def iniciar_rx(sock, mod, enq, edc, callback):
    _, decodificar_mod = MODULACOES[mod]
    _, desenquadrar = ENQUADRAMENTOS[enq]
    _, verify_edc = DETECCAO_CORRECAO[edc]

    dados = sock.recv(65536)
    sinal_recebido = json.loads(dados.decode('utf-8'))

    quadro_demodulado = decodificar_mod(sinal_recebido)
    if isinstance(quadro_demodulado, list):
        quadro_demodulado = ''.join(quadro_demodulado)

    bits_com_edc = desenquadrar(quadro_demodulado)
    edc_ok = verify_edc(bits_com_edc)

    tamanho_edc = TAMANHO_EDC[edc]
    bits_finais = bits_com_edc[:-tamanho_edc]
    texto_final = bits_to_text(bits_finais)

    etapas = {
        'sinal_recebido': sinal_recebido,
        'quadro_demodulado': quadro_demodulado,
        'bits_com_edc': bits_com_edc,
        'edc_ok': edc_ok,
        'bits_finais': bits_finais,
        'texto_final': texto_final,
    }

    callback(etapas)
    sock.close()