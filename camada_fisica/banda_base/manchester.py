V = 1.0

def codificar_manchester(bits):
    sinal = []

    for bit in bits:
        if bit == '0':
            sinal.extend([-V, V])

        elif bit == '1':
            sinal.extend([V, -V])

    return sinal

def decodificar_manchester(sinal):
    bits = []

    for i in range(0, len(sinal), 2):
        par = sinal[i:i+2]

        if par == [-V, V]:
            bits.append('0')

        elif par == [V, -V]:
            bits.append('1')

    return bits