import matplotlib.pyplot as plt
from ask import codificar_ask, decodificar_ask
from utils import text_to_bits

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_ask(bits)
bits_recuperados = decodificar_ask(sinal)

print(f"Original:     {texto}")
print(f"Bits:          {bits}")
print(f"Recuperado:    {bits_recuperados}")
print(f"Igual:         {bits == bits_recuperados}")

plt.figure(figsize=(10, 3))
plt.plot(sinal)
plt.title(f"ASK - bits: {bits}")
plt.xlabel("amostras")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()