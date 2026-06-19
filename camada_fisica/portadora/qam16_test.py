import matplotlib.pyplot as plt
import numpy as np
from qam16 import codificar_qam16, decodificar_qam16, NIVEIS
from utils import text_to_bits

texto = "A"
bits = text_to_bits(texto)
print(f"Original:                 {texto}")
print(f"Bits originais:           {bits}")
print(f"Primeiro grupo (4 bits):  {bits[0:4]}")

sinal = codificar_qam16(bits)
print(f"Tamanho do sinal:         {len(sinal)} amostras")

bits_recuperados = decodificar_qam16(sinal)
print(f"Bits recuperados:         {bits_recuperados}")
print(f"Igual:                    {bits == bits_recuperados}")

plt.figure(figsize=(10, 3))
plt.plot(sinal)
plt.title(f"16-QAM - bits: {bits}")
plt.xlabel("amostras")
plt.ylabel("amplitude")
plt.grid(True)
plt.show()