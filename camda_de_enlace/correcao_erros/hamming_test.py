from hamming import hamming74_codificar, hamming74_decodificar

bits = "10110011"
codigo = hamming74_codificar(bits)
print("Codigo:", codigo)

# simula um erro de 1 bit no primeiro bloco, posicao 3
codigo_com_erro = list(codigo)
codigo_com_erro[2] = '1' if codigo_com_erro[2] == '0' else '0'
codigo_com_erro = ''.join(codigo_com_erro)

decodificado = hamming74_decodificar(codigo_com_erro)
print("Decodificado:", decodificado)
print("Igual ao original?", decodificado == bits)