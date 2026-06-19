import numpy as np

A = 1.0       
F = 2.0          
TAXA_AMOSTRAGEM = 100  
AMOSTRAS_POR_BIT = 50 

def codificar_ask(bits):
    sinal = []
    t_bit = np.linspace(0, 1, AMOSTRAS_POR_BIT)
    for bit in bits:
        amplitude = A if bit == '1' else 0
        onda = amplitude * np.sin(2 * np.pi * F * t_bit)
        sinal.extend(onda)
    return sinal

def decodificar_ask(sinal):
    bits = ''
    for i in range(0, len(sinal), AMOSTRAS_POR_BIT):
        trecho = sinal[i:i+AMOSTRAS_POR_BIT]
        energia = sum(abs(x) for x in trecho) / len(trecho)
        bits += '1' if energia > A/2 else '0'
    return bits