from nrz_polar import codificar_nrz, decodificar_nrz
from utils import bits_to_text, text_to_bits

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_nrz(bits)
bits_recuperados = decodificar_nrz(sinal)
texto_recuperado = bits_to_text(''.join(bits_recuperados))

print(f"Original:    {texto}")
print(f"Bits:        {bits}")
print(f"Sinal:       {sinal}")
print(f"Recuperado:  {texto_recuperado}")