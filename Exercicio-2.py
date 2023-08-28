def ponderada(lista_um, lista_dois):
    x = lista_um[0] * lista_dois[0]
    mult = x
    print(mult)
    i = 1

    while i < len(lista_um) & len(lista_dois):
        x = lista_um[i] * lista_dois[i]
        mult = mult + x
        print(mult)
        i = i + 1

    i = 0
    soma = lista_um[i]
    i = 1
    while i < len(lista_um):
        soma = soma + lista_um[i]
        i = i + 1
    resultado = mult / soma
    return (resultado)


p_um = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
p_dois = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]
media_ponderada = ponderada(p_um, p_dois)
print("O resultado da média ponderada desses valores é :    {}".format(
    media_ponderada))
