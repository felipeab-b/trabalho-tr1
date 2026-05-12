V = 1.0

def codificar_nrz(bits):
    sinal = []
    for bit in bits:
        if bit == '1':
            sinal.append(V)
        else:
            sinal.append(-V)
    return sinal

def decodificar_nrz(sinal):
    bits = []
    for i in sinal:
        if i > 0:
            bits.append('1')
        else:
            bits.append('0')
    return bits
