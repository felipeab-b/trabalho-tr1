import matplotlib.pyplot as plt
# qpsk_test.py
from camada_fisica.portadora.qpsk import codificar_qpsk, decodificar_qpsk
from utils import text_to_bits

texto = "A"
bits = text_to_bits(texto)
sinal = codificar_qpsk(bits)
bits_recuperados = decodificar_qpsk(sinal)

print(f"Original:     {texto}")
print(f"Bits:          {bits}")
print(f"Recuperado:    {bits_recuperados}")
print(f"Igual:         {bits == bits_recuperados}")

plt.figure(figsize=(10, 3))
plt.plot(sinal)
plt.title(f"QPSK - bits: {bits}")
plt.xlabel("amostras")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()