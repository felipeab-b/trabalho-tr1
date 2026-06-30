from camada_fisica.banda_base.manchester import codificar_manchester, decodificar_manchester
from utils import bits_to_text, text_to_bits

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_manchester(bits)
bits_recuperados = decodificar_manchester(sinal)
texto_recuperado = bits_to_text(''.join(bits_recuperados))

print(f"Original:    {texto}")
print(f"Bits:        {bits}")
print(f"Sinal:       {sinal}")
print(f"Recuperado:  {texto_recuperado}")