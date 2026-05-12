def codificar_manchester(bits):
    sinal = []

    for bit in bits:
        if bit == '0':
            sinal.extend([1, 0])

        elif bit == '1':
            sinal.extend([0, 1])

    return sinal

def decodificar_manchester(sinal):
    bits = []

    for i in range(0, len(sinal), 2):
        par = sinal[i:i+2]

        if par == [1, 0]:
            bits.append('0')

        elif par == [0, 1]:
            bits.append('1')

    return bits