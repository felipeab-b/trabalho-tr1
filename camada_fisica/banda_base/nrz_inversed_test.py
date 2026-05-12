from nrz_inversed import codificar_nrz_i, decodificar_nrz_i
from utils import text_to_bits, bits_to_text

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_nrz_i(bits)
bits_recuperados = decodificar_nrz_i(sinal)
texto_recuperado = bits_to_text(''.join(bits_recuperados))

print(f"Original:    {texto}")
print(f"Bits:        {bits}")
print(f"Sinal:       {sinal}")
print(f"Recuperado:  {texto_recuperado}")