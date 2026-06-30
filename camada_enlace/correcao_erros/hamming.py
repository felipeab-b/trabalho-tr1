def hamming74_codificar(bits):
    while len(bits) % 4 != 0:
        bits += '0'

    codigo = ''

    for i in range(0, len(bits), 4):
        d1, d2, d3, d4 = (int(b) for b in bits[i:i+4])

        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p3 = d2 ^ d3 ^ d4

        bloco = f"{p1}{p2}{d1}{p3}{d2}{d3}{d4}"
        codigo += bloco

    return codigo


def hamming74_decodificar(codigo):
    bits_originais = ''

    for i in range(0, len(codigo), 7):
        bloco = [int(b) for b in codigo[i:i+7]]
        p1, p2, d1, p3, d2, d3, d4 = bloco

        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4

        posicao_erro = s3 * 4 + s2 * 2 + s1

        if posicao_erro != 0:
            bloco[posicao_erro - 1] ^= 1  

        _, _, d1, _, d2, d3, d4 = bloco
        bits_originais += f"{d1}{d2}{d3}{d4}"

    return bits_originais