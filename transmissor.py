import json
from camada_fisica.banda_base.nrz_polar import codificar_nrz
from camada_fisica.banda_base.utils import text_to_bits

def iniciar_tx(sock, texto):
    bits = text_to_bits(texto)
    sinal = codificar_nrz(bits)
    dados = json.dumps(sinal).encode('utf-8')
    sock.sendall(dados)
    sock.close()