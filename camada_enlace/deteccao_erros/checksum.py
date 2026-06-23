def add_checksum(bits):
    soma = 0
    for i in range(0, len(bits), 8):
        segmento = bits[i:i+8].ljust(8, '0')  
        soma += int(segmento, 2)
    while soma > 0xFF:
        soma = (soma & 0xFF) + (soma >> 8)
    checksum = soma ^ 0xFF
    checksum_bits = format(checksum, '08b')
    return bits + checksum_bits

def verify_checksum(bits):
    if len(bits) < 8:
        return False  
    data_bits = bits[:-8]
    checksum_bits = bits[-8:]
    soma = 0
    for i in range(0, len(data_bits), 8):
        segmento = data_bits[i:i+8].ljust(8, '0')  
        soma += int(segmento, 2)
    while soma > 0xFF:
        soma = (soma & 0xFF) + (soma >> 8)
    checksum_calculado = soma ^ 0xFF
    checksum_recebido = int(checksum_bits, 2)
    return checksum_calculado == checksum_recebido