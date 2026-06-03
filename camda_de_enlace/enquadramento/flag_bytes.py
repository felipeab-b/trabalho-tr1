FLAG = '01111110'
ESC  = '00011101'

def enquadrar_flag_bytes(bits):
    dados_enquadrados = FLAG
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == FLAG:
            dados_enquadrados += ESC + FLAG
        elif byte == ESC:
            dados_enquadrados += ESC + ESC
        else:
            dados_enquadrados += byte
    dados_enquadrados += FLAG
    return dados_enquadrados

def desenquadrar_flag_bytes(bits):
    if bits.startswith(FLAG) and bits.endswith(FLAG):
        dados_desenquadrados = ''
        i = len(FLAG)
        while i < len(bits) - len(FLAG):
            byte = bits[i:i+8]
            if byte == ESC:
                proximo = bits[i+8:i+16]
                dados_desenquadrados += proximo
                i += 16
            else:
                dados_desenquadrados += byte
                i += 8
        return dados_desenquadrados
    else:
        raise ValueError("Os dados não estão corretamente enquadrados com FLAG.")