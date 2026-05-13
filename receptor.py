import json
from camada_fisica.banda_base.nrz_polar import decodificar_nrz
from camada_fisica.banda_base.utils import bits_to_text

def iniciar_rx(sock):
    dados = sock.recv(65536)
    sinal = json.loads(dados.decode('utf-8'))
    bits = decodificar_nrz(sinal)
    texto = bits_to_text(''.join(bits))
    print(f"Texto recebido: {texto}")
    sock.close()