import numpy as np
import matplotlib.pyplot as plt
from camada_fisica.portadora.qam16 import codificar_qam16, decodificar_qam16, NIVEIS
from camada_fisica.banda_base.nrz_polar import codificar_nrz, decodificar_nrz
from utils import text_to_bits

AMOSTRAS_POR_BIT = 50

texto = "A"
bits = text_to_bits(texto)

sinal_base = codificar_nrz(bits)
sinal_qam16 = codificar_qam16(sinal_base)
sinal_base_recuperado = decodificar_qam16(sinal_qam16)
bits_recuperados = decodificar_nrz(sinal_base_recuperado)
bits_recuperados = ''.join(bits_recuperados) if isinstance(bits_recuperados, list) else bits_recuperados

print(f"Original:           {texto}")
print(f"Bits:                {bits}")
print(f"Recuperado:          {bits_recuperados}")
print(f"Igual:               {bits == bits_recuperados}")

pontos = []
for i in range(0, len(sinal_base), 4):
    grupo_niveis = sinal_base[i:i+4]
    grupo_bits = ''.join('1' if n > 0 else '0' for n in grupo_niveis)
    I = NIVEIS[grupo_bits[0:2]]
    Q = NIVEIS[grupo_bits[2:4]]
    pontos.append((I, Q))

sinal_base_expandido = np.repeat(sinal_base, AMOSTRAS_POR_BIT)

fig1, axs = plt.subplots(2, 1, figsize=(10, 5))
axs[0].plot(sinal_base_expandido)
axs[0].set_title(f"Banda-base (NRZ) - bits: {bits}")
axs[0].set_ylabel("amplitude")
axs[0].grid(True)

axs[1].plot(sinal_qam16)
axs[1].set_title(f"Portadora (16-QAM) - {len(sinal_qam16)} amostras (4 bits/simbolo)")
axs[1].set_xlabel("amostras")
axs[1].set_ylabel("amplitude")
axs[1].grid(True)
plt.tight_layout()

fig2 = plt.figure(figsize=(5, 5))
for ib in NIVEIS.values():
    for qb in NIVEIS.values():
        plt.scatter(ib, qb, color='lightgray', s=80)

xs = [p[0] for p in pontos]
ys = [p[1] for p in pontos]
plt.plot(xs, ys, 'o-', color='#5b8cff', markersize=12, linewidth=1, alpha=0.7)
for idx, (x, y) in enumerate(pontos):
    plt.annotate(str(idx), (x, y), textcoords="offset points", xytext=(8, 8))

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.xlabel("I (em fase)")
plt.ylabel("Q (quadratura)")
plt.title("Constelação 16-QAM")
plt.grid(True, alpha=0.3)

plt.show()