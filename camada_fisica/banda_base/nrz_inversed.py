def codificar_nrz_i(bits):
    sinal = []
    nivel = -1

    for bit in bits:
        if bit == '1':
            nivel *= -1
        sinal.append(nivel)

    return sinal

def decodificar_nrz_i(sinal):
    bits = []

    nivel_anterior = -1

    for nivel_atual in sinal:
        if nivel_atual != nivel_anterior:
            bits.append('1')
        else:
            bits.append('0')

        nivel_anterior = nivel_atual

    return bits