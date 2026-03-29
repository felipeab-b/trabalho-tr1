def texto_para_bits(texto):
    bits = [0] * (len(texto) * 8)
    for i, num in enumerate(ord(char) for char in texto):
        for j in range(8):
            bits[i * 8 + j] = (num >> (7 - j)) & 1
    return bits
