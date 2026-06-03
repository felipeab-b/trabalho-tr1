def add_paridade(bits):
    num_1s = bits.count('1')
    paridade = '0' if num_1s % 2 == 0 else '1'
    return bits + paridade

def verify_paridade(bits):
    if len(bits) < 2:
        raise ValueError("A string de bits deve conter pelo menos um bit de dados e um bit de paridade.")
    data_bits = bits[:-1]
    paridade_bit = bits[-1]
    num_1s = data_bits.count('1')
    paridade_calculada = '0' if num_1s % 2 == 0 else '1'
    return paridade_bit == paridade_calculada