def calcular_media(dados):
    soma = sum(dados)
    media = soma / len(dados)
    return media


def calcular_variancia_amostral(dados):
    media = calcular_media(dados)
    diferenca_quad = [(x - media) ** 2 for x in dados]
    variancia = sum(diferenca_quad) / (len(dados) - 1)
    return variancia

va = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
variancia_amostral = calcular_variancia_amostral(va)
print("O resultado da variancia amostral desses valores é :   {:.2f}".format(
    variancia_amostral))


def calcular_variancia_populacional(dados):
    media = calcular_media(dados)
    diferenca_quad = [(x - media) ** 2 for x in dados]
    variancia = sum(diferenca_quad) / len(dados)
    return variancia

vp = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
variancia_populacional = calcular_variancia_populacional(vp)
print("O resultado da variancia populacional desses valores é :   {:.2f}".format(
    variancia_populacional))


def calcular_desvio_padrao_amostral(dados):
    media = calcular_media(dados)
    diferenca_quad = [(x - media) ** 2 for x in dados]
    variancia = sum(diferenca_quad) / (len(dados) - 1)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

dvpa = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
desvio_padrao_amostral = calcular_desvio_padrao_amostral(dvpa)
print("O resultado da desvio padrão amostral desses valores é :   {:.2f}".format(
    desvio_padrao_amostral))


def calcular_desvio_padrao_populacional(dados):
    media = calcular_media(dados)
    diferenca_quad = [(x - media) ** 2 for x in dados]
    variancia = sum(diferenca_quad) / len(dados)
    desvio_padrao = variancia ** 0.5
    return desvio_padrao

desvio_p = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
desvio_padrao_populacional = calcular_desvio_padrao_populacional(desvio_p)
print("O resultado da desvio padrão populacional desses valores é :   {:.2f}".format(
    desvio_padrao_populacional))


def calcular_incerteza_media(dados):
    desvio_padrao_amostral = calcular_desvio_padrao_amostral(dados)
    incerteza_media = desvio_padrao_amostral / (len(dados) ** 0.5)
    return incerteza_media

incert_med = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
incerteza_media = calcular_incerteza_media(incert_med)
print("O resultado da incerteza da média desses valores é :   {:.2f}".format(
    incerteza_media))