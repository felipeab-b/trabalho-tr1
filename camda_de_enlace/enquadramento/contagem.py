def enquadrar(bits):
    quantidade_bytes = len(bits) // 8
    header = format(quantidade_bytes, '08b')
    return header + bits

def desenquadrar(bits):
    header = bits[:8]
    quantidade_bytes = int(header, 2)
    payload = bits[8:8 + quantidade_bytes * 8]
    return payload

