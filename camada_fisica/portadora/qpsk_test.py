import numpy as np
import matplotlib.pyplot as plt
from camada_fisica.portadora.qpsk import codificar_qpsk, decodificar_qpsk
from camada_fisica.banda_base.nrz_polar import codificar_nrz, decodificar_nrz

AMOSTRAS_POR_BIT = 50

bits = "00011110"  

sinal_base = codificar_nrz(bits)
sinal_qpsk = codificar_qpsk(sinal_base)
sinal_base_recuperado = decodificar_qpsk(sinal_qpsk)
bits_recuperados = decodificar_nrz(sinal_base_recuperado)
bits_recuperados = ''.join(bits_recuperados) if isinstance(bits_recuperados, list) else bits_recuperados

print(f"Bits:       {bits}")
print(f"Recuperado: {bits_recuperados}")
print(f"Igual:      {bits == bits_recuperados}")

sinal_base_expandido = np.repeat(sinal_base, AMOSTRAS_POR_BIT)

fig, axs = plt.subplots(2, 1, figsize=(10, 5))

axs[0].plot(sinal_base_expandido)
axs[0].set_title(f"Banda-base (NRZ) - bits: {bits}")
axs[0].grid(True)

axs[1].plot(sinal_qpsk)
axs[1].set_title("Portadora (QPSK) - 4 simbolos distintos: 00, 01, 11, 10")
axs[1].set_xlabel("amostras")
axs[1].grid(True)

for x in [50, 100, 150]:
    axs[1].axvline(x, color='red', linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()