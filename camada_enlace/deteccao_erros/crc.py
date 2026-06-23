def crc32(bits):
    POLY = 0xEDB88320
    crc = 0xFFFFFFFF

    bits = bits.ljust((len(bits) + 7) // 8 * 8, '0')

    for i in range(0, len(bits), 8):
        byte = int(bits[i:i+8], 2)
        crc ^= byte

        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ POLY
            else:
                crc >>= 1

    return crc ^ 0xFFFFFFFF


def add_crc(bits):
    crc = crc32(bits)
    crc_bits = format(crc, '032b')
    return bits + crc_bits


def verify_crc(bits):
    if len(bits) < 32:
        return False

    data_bits = bits[:-32]
    crc_recebido = bits[-32:]

    crc_calculado = crc32(data_bits)

    return format(crc_calculado, '032b') == crc_recebido