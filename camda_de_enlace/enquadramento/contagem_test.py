from contagem import enquadrar, desenquadrar
from utils import bits_to_text, text_to_bits

texto = "Teste"
bits = text_to_bits(texto)
msg = enquadrar(bits)
payload = desenquadrar(msg)

print(f"Original:    {texto}")
print(f"Bits:        {bits}")
print(f"Msg:       {msg}")
print(f"Payload:  {payload}")