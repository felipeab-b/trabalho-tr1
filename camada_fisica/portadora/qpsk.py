import numpy as np

A = 1.0
F = 2.0
AMOSTRAS_POR_SIMBOLO = 50

FASES = {
    '00': np.pi/4,
    '01': 3*np.pi/4,
    '11': 5*np.pi/4,
    '10': 7*np.pi/4,
}

def codificar_qpsk(sinal_base):
    if len(sinal_base) % 2 != 0:
        sinal_base = list(sinal_base) + [-A]

    sinal = []
    t = np.linspace(0, 1, AMOSTRAS_POR_SIMBOLO)
    for i in range(0, len(sinal_base), 2):
        par_niveis = sinal_base[i:i+2]
        par_bits = ''.join('1' if nivel > 0 else '0' for nivel in par_niveis)
        fase = FASES[par_bits]
        onda = A * np.cos(2 * np.pi * F * t + fase)
        sinal.extend(onda)
    return sinal

def decodificar_qpsk(sinal):
    sinal_base = []
    t = np.linspace(0, 1, AMOSTRAS_POR_SIMBOLO)
    referencias = {par: A * np.cos(2 * np.pi * F * t + fase) for par, fase in FASES.items()}

    for i in range(0, len(sinal), AMOSTRAS_POR_SIMBOLO):
        trecho = np.array(sinal[i:i+AMOSTRAS_POR_SIMBOLO])
        melhor_par = None
        melhor_correlacao = -np.inf
        for par, ref in referencias.items():
            correlacao = np.dot(trecho, ref)
            if correlacao > melhor_correlacao:
                melhor_correlacao = correlacao
                melhor_par = par
        for bit in melhor_par:
            sinal_base.append(A if bit == '1' else -A)
    return sinal_base