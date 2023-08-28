def mediana(num):
    num_ordenado = sorted(num)
    tamanho = len(num_ordenado)
    
    if tamanho % 2 == 0:
        meio1 = num_ordenado[tamanho // 2 - 1]
        meio2 = num_ordenado[tamanho // 2]
        mediana = (meio1 + meio2) / 2
    else:
        mediana = num_ordenado[tamanho // 2]
    
    return mediana

me = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
m_mediana = mediana(me)
print("O resultado da mediana desses valores é: {}".format(m_mediana))


def moda(num):
    frequencias = {}
    for n in num:
        if n in frequencias:
            frequencias[n] += 1
        else:
            frequencias[n] = 1

    moda = None
    max_frequencia = 0

    for numero, frequencia in frequencias.items():
        if frequencia > max_frequencia:
            moda = numero
            max_frequencia = frequencia

    return moda

mo = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
m_moda = moda(mo)
print("O resultado da moda desses valores é: {}".format(m_moda))

