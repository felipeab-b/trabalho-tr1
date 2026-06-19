import numpy as np

A = 1.0
F1 = 4.0  
F0 = 2.0  
AMOSTRAS_POR_BIT = 50

def codificar_fsk(bits):
    sinal = []
    t_bit = np.linspace(0, 1, AMOSTRAS_POR_BIT)
    for bit in bits:
        freq = F1 if bit == '1' else F0
        onda = A * np.sin(2 * np.pi * freq * t_bit)
        sinal.extend(onda)
    return sinal

def decodificar_fsk(sinal):
    bits = ''
    for i in range(0, len(sinal), AMOSTRAS_POR_BIT):
        trecho = sinal[i:i+AMOSTRAS_POR_BIT]
        cruzamentos = 0
        for j in range(1, len(trecho)):
            if trecho[j-1] * trecho[j] < 0:
                cruzamentos += 1
        bits += '1' if cruzamentos > 6 else '0'
    return bits