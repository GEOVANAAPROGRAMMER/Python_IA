import numpy as np


def ponderada(lista_um, lista_dois):
    lista_um = np.array(lista_um)
    dois = np.array(lista_dois)
    resultado = np.average(lista_um, weights=lista_dois)
    return (resultado)


p_um = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
p_dois = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]
media_ponderada = ponderada(p_um, p_dois)
print("O resultado da média ponderada desses valores é :    {:.2f}".format(
    media_ponderada))
