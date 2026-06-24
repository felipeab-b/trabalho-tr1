import numpy as np

A = 1.0
F = 2.0
AMOSTRAS_POR_BIT = 50

def codificar_ask(sinal_base):
    sinal_expandido = np.repeat(sinal_base, AMOSTRAS_POR_BIT)
    t = np.linspace(0, len(sinal_base), len(sinal_expandido))
    portadora = np.sin(2 * np.pi * F * t)

    sinal = []
    for nivel, onda_portadora in zip(sinal_expandido, portadora):
        amplitude = A if nivel > 0 else 0
        sinal.append(amplitude * onda_portadora)
    return sinal

def decodificar_ask(sinal):
    sinal_base = []
    for i in range(0, len(sinal), AMOSTRAS_POR_BIT):
        trecho = sinal[i:i+AMOSTRAS_POR_BIT]
        energia = sum(abs(x) for x in trecho) / len(trecho)
        sinal_base.append(A if energia > A/2 else -A)
    return sinal_base