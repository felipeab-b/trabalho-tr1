from camada_enlace.enquadramento.contagem import enquadrar_contagem, desenquadrar_contagem
from utils import bits_to_text, text_to_bits

texto = "Teste"
bits = text_to_bits(texto)
msg = enquadrar_contagem(bits)
payload = desenquadrar_contagem(msg)

print(f"Original:    {texto}")
print(f"Bits:        {bits}")
print(f"Msg:       {msg}")
print(f"Payload:  {payload}")