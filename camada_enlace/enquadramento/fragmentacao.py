from camada_enlace.enquadramento.contagem import enquadrar_contagem
from camada_enlace.enquadramento.flag_bytes import FLAG as FLAG_BYTES, ESC
from camada_enlace.enquadramento.flag_bits import FLAG as FLAG_BITS


def fragmentar(bits, tamanho_maximo):
    pedacos = []
    for i in range(0, len(bits), tamanho_maximo):
        pedacos.append(bits[i:i + tamanho_maximo])
    return pedacos


def enquadrar_multiplo_contagem(bits, tamanho_maximo):
    pedacos = fragmentar(bits, tamanho_maximo)
    quadros = [enquadrar_contagem(pedaco) for pedaco in pedacos]
    return ''.join(quadros)


def desenquadrar_multiplo_contagem(bits_totais):
    payloads = []
    i = 0
    while i < len(bits_totais):
        header = bits_totais[i:i + 16]
        if len(header) < 16:
            break
        quantidade_bits = int(header, 2)
        payload = bits_totais[i + 16:i + 16 + quantidade_bits]
        payloads.append(payload)
        i += 16 + quantidade_bits
    return ''.join(payloads)


def enquadrar_multiplo_flag_bytes(bits, tamanho_maximo):
    from camada_enlace.enquadramento.flag_bytes import enquadrar_flag_bytes
    pedacos = fragmentar(bits, tamanho_maximo)
    quadros = [enquadrar_flag_bytes(pedaco) for pedaco in pedacos]
    return ''.join(quadros)


def desenquadrar_multiplo_flag_bytes(bits_totais):
    from camada_enlace.enquadramento.flag_bytes import desenquadrar_flag_bytes
    payloads = []
    i = 0
    n = len(bits_totais)
    while i < n:
        if bits_totais[i:i + 8] != FLAG_BYTES:
            break
        j = i + 8
        while j < n:
            if bits_totais[j:j + 8] == FLAG_BYTES:
                if bits_totais[j - 8:j] == ESC:
                    j += 8
                    continue
                break
            j += 8
        fim_quadro = j + 8
        quadro = bits_totais[i:fim_quadro]
        payloads.append(desenquadrar_flag_bytes(quadro))
        i = fim_quadro
    return ''.join(payloads)


def enquadrar_multiplo_flag_bits(bits, tamanho_maximo):
    from camada_enlace.enquadramento.flag_bits import enquadrar_flag_bits
    pedacos = fragmentar(bits, tamanho_maximo)
    quadros = [enquadrar_flag_bits(pedaco) for pedaco in pedacos]
    return ''.join(quadros)


def desenquadrar_multiplo_flag_bits(bits_totais):
    from camada_enlace.enquadramento.flag_bits import desenquadrar_flag_bits
    payloads = []
    i = 0
    n = len(bits_totais)
    tam_flag = len(FLAG_BITS)
    while i < n:
        if bits_totais[i:i + tam_flag] != FLAG_BITS:
            break
        j = bits_totais.find(FLAG_BITS, i + tam_flag)
        if j == -1:
            break
        fim_quadro = j + tam_flag
        quadro = bits_totais[i:fim_quadro]
        payloads.append(desenquadrar_flag_bits(quadro))
        i = fim_quadro
    return ''.join(payloads)