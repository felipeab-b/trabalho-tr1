FLAG = '01111110'

def enquadrar_flag_bits(bits):
    resultado = ''
    contagem = 0
    for bit in bits:
        resultado += bit
        if bit == '1':
            contagem += 1
        else:
            contagem = 0
        if contagem == 5:
            resultado += '0'
            contagem = 0
    return FLAG + resultado + FLAG

def desenquadrar_flag_bits(bits):
    if bits.startswith(FLAG) and bits.endswith(FLAG):
        bits = bits[len(FLAG):-len(FLAG)]
        resultado = ''
        contagem = 0
        for bit in bits:
            if contagem == 5 and bit == '0':
                contagem = 0
                continue
            resultado += bit
            if bit == '1':
                contagem += 1
            else:
                contagem = 0
        return resultado
    else:
        raise ValueError("Os bits não estão corretamente enquadrados com FLAG.")