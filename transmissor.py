import json
from camada_fisica.banda_base.nrz_polar import codificar_nrz
from camada_fisica.banda_base.utils import text_to_bits

def iniciar_tx(sock):
    text = input("Digite o texto: ")
    bits = text_to_bits(text)
    sinal = codificar_nrz(bits)
    data = json.dumps(sinal).encode('utf-8')
    sock.sendall(data)
    sock.close()