
import numpy as np

def aplicar_ruido(sinal, media=0.0, desvio_padrao=0.0):
    if desvio_padrao == 0:
        return sinal

    sinal_array = np.array(sinal, dtype=float)
    ruido = np.random.normal(media, desvio_padrao, size=sinal_array.shape)
    sinal_com_ruido = sinal_array + ruido
    return sinal_com_ruido.tolist()