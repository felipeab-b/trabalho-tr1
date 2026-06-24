import numpy as np
import matplotlib.pyplot as plt
from camada_fisica.portadora.ask import codificar_ask, decodificar_ask
from camada_fisica.banda_base.nrz_polar import codificar_nrz, decodificar_nrz
from utils import text_to_bits

AMOSTRAS_POR_BIT = 50

texto = "A"
bits = text_to_bits(texto)

sinal_base = codificar_nrz(bits)
sinal_ask = codificar_ask(sinal_base)
sinal_base_recuperado = decodificar_ask(sinal_ask)
bits_recuperados = decodificar_nrz(sinal_base_recuperado)
bits_recuperados = ''.join(bits_recuperados) if isinstance(bits_recuperados, list) else bits_recuperados

print(f"Original:           {texto}")
print(f"Bits:                {bits}")
print(f"Sinal base (NRZ):    {sinal_base}")
print(f"Recuperado:          {bits_recuperados}")
print(f"Igual:               {bits == bits_recuperados}")

sinal_base_expandido = np.repeat(sinal_base, AMOSTRAS_POR_BIT)

fig, axs = plt.subplots(2, 1, figsize=(10, 5), sharex=True)

axs[0].plot(sinal_base_expandido)
axs[0].set_title(f"Banda-base (NRZ) - bits: {bits}")
axs[0].set_ylabel("amplitude")
axs[0].grid(True)

axs[1].plot(sinal_ask)
axs[1].set_title("Portadora (ASK)")
axs[1].set_xlabel("amostras")
axs[1].set_ylabel("amplitude")
axs[1].grid(True)

plt.tight_layout()
plt.show()