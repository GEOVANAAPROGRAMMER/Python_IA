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


p_um = [5, 16, 3, 1]
p_dois = [1100, 2000, 5500, 12500]
media_ponderada = ponderada(p_um, p_dois)
print("O resultado da média ponderada desses valores é :    {}".format(
    media_ponderada))
