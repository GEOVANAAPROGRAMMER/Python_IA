def calcular_media(dados):
    soma = sum(dados)
    media = soma / len(dados)
    return media


def calcular_variancia_amostral(dados):
    media = calcular_media(dados)
    diferenca_quad = [(x - media) ** 2 for x in dados]
    variancia = sum(diferenca_quad) / (len(dados) - 1)
    return variancia

dados = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
variancia_amostral = calcular_variancia_amostral(dados)
print("O resultado da variancia amostral desses valores é :   {:.2f}".format(
    variancia_amostral))