import numpy as np

A = 1.0
F = 2.0
AMOSTRAS_POR_SIMBOLO = 50

NIVEIS = {'00': -3, '01': -1, '11': 1, '10': 3}

def codificar_qam16(sinal_base):
    while len(sinal_base) % 4 != 0:
        sinal_base = list(sinal_base) + [-A]

    sinal = []
    t = np.linspace(0, 1, AMOSTRAS_POR_SIMBOLO, endpoint=False)
    for i in range(0, len(sinal_base), 4):
        grupo_niveis = sinal_base[i:i+4]
        grupo_bits = ''.join('1' if nivel > 0 else '0' for nivel in grupo_niveis)
        I = NIVEIS[grupo_bits[0:2]]
        Q = NIVEIS[grupo_bits[2:4]]
        onda = I * np.cos(2*np.pi*F*t) + Q * np.sin(2*np.pi*F*t)
        sinal.extend(onda)
    return sinal

def decodificar_qam16(sinal):
    sinal_base = []
    t = np.linspace(0, 1, AMOSTRAS_POR_SIMBOLO, endpoint=False)
    cos_ref = np.cos(2*np.pi*F*t)
    sin_ref = np.sin(2*np.pi*F*t)
    energia_cos = np.dot(cos_ref, cos_ref)
    energia_sin = np.dot(sin_ref, sin_ref)

    niveis_para_bits = {v: k for k, v in NIVEIS.items()}
    niveis_validos = list(NIVEIS.values())

    def nivel_mais_proximo(valor):
        return min(niveis_validos, key=lambda nivel: abs(nivel - valor))

    for i in range(0, len(sinal), AMOSTRAS_POR_SIMBOLO):
        trecho = np.array(sinal[i:i+AMOSTRAS_POR_SIMBOLO])
        proj_I = np.dot(trecho, cos_ref) / energia_cos
        proj_Q = np.dot(trecho, sin_ref) / energia_sin
        I_estimado = nivel_mais_proximo(proj_I)
        Q_estimado = nivel_mais_proximo(proj_Q)
        grupo_bits = niveis_para_bits[I_estimado] + niveis_para_bits[Q_estimado]
        for bit in grupo_bits:
            sinal_base.append(A if bit == '1' else -A)
    return sinal_base