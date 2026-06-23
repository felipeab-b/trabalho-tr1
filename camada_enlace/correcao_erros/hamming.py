def hamming74_codificar(bits):
    """
    Codifica uma string de bits em blocos de Hamming(7,4).
    Completa com zeros se o tamanho nao for multiplo de 4.
    Retorna uma string com blocos de 7 bits cada.
    """
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
    """
    Decodifica uma string com blocos de 7 bits (Hamming 7,4),
    corrigindo um erro de bit unico por bloco, se houver.
    Retorna a string de bits de dados originais (4 bits por bloco).
    """
    bits_originais = ''

    for i in range(0, len(codigo), 7):
        bloco = [int(b) for b in codigo[i:i+7]]
        p1, p2, d1, p3, d2, d3, d4 = bloco

        # Recalcula os bits de sindrome
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4

        # A sindrome (s3 s2 s1) em binario indica a posicao do erro (1-indexada)
        posicao_erro = s3 * 4 + s2 * 2 + s1

        if posicao_erro != 0:
            bloco[posicao_erro - 1] ^= 1  # corrige o bit invertido

        # Apos correcao, extrai os bits de dados nas posicoes 3,5,6,7 (1-indexado)
        _, _, d1, _, d2, d3, d4 = bloco
        bits_originais += f"{d1}{d2}{d3}{d4}"

    return bits_originais