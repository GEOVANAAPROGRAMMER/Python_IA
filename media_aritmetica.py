def aritimetica(num):
    soma = 0
    i = 0

    while i < len(num):
        soma = soma + num[i]
        i = i + 1
        qtd_itens = i
        media_ari = soma / qtd_itens
    return (media_ari)


a = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

media_aritmetica = aritimetica(a)
print("O resultado da média aritmética desses valores é :   {:.2f}".format(
    media_aritmetica))


def geometrica(num):
    mult = 1
    i = 0

    while i < len(num):
        mult = mult * num[i]
        i = i + 1
        qtd_itens = i
    raiz = mult ** (1/qtd_itens)
    return (raiz)


g = [4, 6, 9]
media_geometrica = geometrica(g)
print("O resultado da média geométrica desses valores é :    {:.2f}".format(
    media_geometrica))
