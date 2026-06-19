import matplotlib.pyplot as plt
from fsk import codificar_fsk, decodificar_fsk
from utils import text_to_bits

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_fsk(bits)
bits_recuperados = decodificar_fsk(sinal)

print(f"Original:     {texto}")
print(f"Bits:          {bits}")
print(f"Recuperado:    {bits_recuperados}")
print(f"Igual:         {bits == bits_recuperados}")

plt.figure(figsize=(10, 3))
plt.plot(sinal)
plt.title(f"FSK - bits: {bits}")
plt.xlabel("amostras")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()