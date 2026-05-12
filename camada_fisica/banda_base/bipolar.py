def codificar_bipolar(bits):
    sinal = []
    ultimo = -1

    for bit in bits:
        if bit == '1':
            ultimo *= -1
            sinal.append(ultimo)
        else:
            sinal.append(0)

    return sinal

def decodificar_bipolar(sinal):
    bits = []

    for nivel in sinal:
        if nivel == 0:
            bits.append('0')
        else:
            bits.append('1')

    return bits