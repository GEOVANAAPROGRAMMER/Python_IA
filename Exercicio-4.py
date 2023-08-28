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


def calcular_media(dados):
    soma = sum(dados)
    media = soma / len(dados)
    return media

def calcular_variancia_populacional(dados):
    media = calcular_media(dados)
    diferenca_quad = [(x - media) ** 2 for x in dados]
    variancia = sum(diferenca_quad) / len(dados)
    return variancia

vp = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
variancia_populacional = calcular_variancia_populacional(vp)
print("O resultado da variancia populacional desses valores é :   {:.2f}".format(
    variancia_populacional))