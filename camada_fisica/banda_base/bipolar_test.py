# bipolar_test.py
from camada_fisica.banda_base.bipolar import codificar_bipolar, decodificar_bipolar
from utils import text_to_bits, bits_to_text

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_bipolar(bits)
bits_recuperados = decodificar_bipolar(sinal)
texto_recuperado = bits_to_text(''.join(bits_recuperados))

print(f"Original:    {texto}")
print(f"Bits:        {bits}")
print(f"Sinal:       {sinal}")
print(f"Recuperado:  {texto_recuperado}")