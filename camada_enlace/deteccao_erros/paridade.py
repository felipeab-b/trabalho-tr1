def add_paridade(bits):
    num_1s = bits.count('1')
    paridade = '0' if num_1s % 2 == 0 else '1'
    return bits + paridade.zfill(8)

def verify_paridade(bits):
    if len(bits) < 8:
        raise ValueError(...)
    data_bits = bits[:-8]
    paridade_bit = bits[-1]    
    num_1s = data_bits.count('1')
    paridade_calculada = '0' if num_1s % 2 == 0 else '1'
    return paridade_bit == paridade_calculada