import statistics as st


def mediana(num):
    resultado = st.median(num)
    return (resultado)


def moda(num):
    resultado = st.mode(num)
    return (resultado)


me = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
m_mediana = mediana(me)
print("O resultado da mediana desses valores é :    {}".format(
    m_mediana))

mo = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
m_moda = moda(mo)
print("O resultado da moda desses valores é :    {}".format(
    m_moda))
