# flag_bytes_test.py
from camada_enlace.enquadramento.flag_bytes import enquadrar_flag_bytes, desenquadrar_flag_bytes
from utils import bits_to_text, text_to_bits

FLAG = '01111110'
ESC  = '00011101'

VERMELHO = '\033[91m'
AMARELO  = '\033[93m'
RESET    = '\033[0m'

def colorir(msg):
    resultado = ''
    i = 0
    while i < len(msg):
        chunk = msg[i:i+8]
        if chunk == FLAG:
            resultado += VERMELHO + chunk + RESET
        elif chunk == ESC:
            resultado += AMARELO + chunk + RESET
        else:
            resultado += chunk
        i += 8
    return resultado

texto = "Teste"
bits = text_to_bits(texto)
msg = enquadrar_flag_bytes(bits)
payload = desenquadrar_flag_bytes(msg)

print(f"Original: {texto}")
print(f"Bits:     {bits}")
print(f"Msg:      {colorir(msg)}")
print(f"Payload:  {payload}")

print("")

texto2 = text_to_bits("A") 
payload_com_flag = texto2 + FLAG + texto2 + ESC + texto2

print(f"Original: {colorir(payload_com_flag)}")
msg2 = enquadrar_flag_bytes(payload_com_flag)
print(f"Enquadrado:       {colorir(msg2)}")
recuperado2 = desenquadrar_flag_bytes(msg2)
print(f"Desenquadrado:    {colorir(recuperado2)}")
print(f"Igual original:   {payload_com_flag == recuperado2}")