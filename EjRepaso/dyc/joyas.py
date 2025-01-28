def balanza(arr1, arr2):
    suma1 = sum(arr1)
    suma2 = sum(arr2)

    if suma1 > suma2:
        return 1
    elif suma2 > suma1:
        return -1
    else:
        return 0
def encontrar_joya_dyc(joyas, inicio, fin):
    if fin-inicio == 1:
        return fin-1

    mitad = (inicio+fin) // 2

    joyas_izq = joyas[inicio:mitad]
    joyas_der = joyas[mitad:fin]

    if len(joyas_izq) != len(joyas_der):
        joya_quitada = fin-1
        joyas_der.pop()

    resultado_balanza = balanza(joyas_izq, joyas_der)
    if resultado_balanza == 1:
        return encontrar_joya_dyc(joyas, inicio, mitad)
    elif resultado_balanza == -1:
        return encontrar_joya_dyc(joyas, mitad, fin)
    else:
        return joya_quitada

def encontrar_joya(joyas):
    inicio = 0
    fin = len(joyas)

    return encontrar_joya_dyc(joyas, inicio,fin)



joyas = [0,1,0]
print(encontrar_joya(joyas))