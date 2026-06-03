from flag_bits import enquadrar_flag_bits, desenquadrar_flag_bits
from utils import bits_to_text, text_to_bits

FLAG = '01111110'

VERMELHO = '\033[91m'
RESET    = '\033[0m'

def colorir(msg):
    resultado = ''
    i = 0
    while i < len(msg):
        chunk = msg[i:i+8]
        if chunk == FLAG:
            resultado += VERMELHO + chunk + RESET
            i += 8
        else:
            resultado += msg[i]
            i += 1
    return resultado

texto = "Teste"
bits = text_to_bits(texto)
msg = enquadrar_flag_bits(bits)
payload = desenquadrar_flag_bits(msg)

print(f"Original: {texto}")
print(f"Bits:     {bits}")
print(f"Msg:      {colorir(msg)}")
print(f"Payload:  {payload}")
print(f"Igual:    {bits == payload}")

print("")

bits2 = '01111110' + text_to_bits("A")
msg2 = enquadrar_flag_bits(bits2)
payload2 = desenquadrar_flag_bits(msg2)
print(f"Original:  {bits2}")
print(f"Msg:       {colorir(msg2)}")
print(f"Payload:   {payload2}")
print(f"Igual:     {bits2 == payload2}")