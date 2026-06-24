def enquadrar_contagem(bits):
    quantidade_bits = len(bits)
    header = format(quantidade_bits, '016b')
    return header + bits

def desenquadrar(bits):
    header = bits[:16]
    quantidade_bits = int(header, 2)
    payload = bits[16:16 + quantidade_bits]
    return payload