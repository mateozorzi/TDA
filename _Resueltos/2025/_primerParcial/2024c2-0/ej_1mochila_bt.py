"""
Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
máxima y cuyo peso no exceda el valor de W
"""

def suma_restante(elementos, indice):
    restante = 0
    for e in range(indice, len(elementos)):
        restante += elementos[e][1]

    return restante


def mochila_bt(elementos, k, w, indice, parcial, sol, peso_parcial, peso_sol, valor_parcial, valor_solucion):
    if len(parcial) >= k and valor_parcial > valor_solucion:
        return parcial[:], valor_parcial, peso_parcial
    
    if indice >= len(elementos):
        return sol, valor_solucion, peso_sol
    
    if valor_parcial + suma_restante(elementos, indice) <= valor_solucion:
        return sol, valor_solucion, peso_sol

    if peso_parcial + elementos[indice] <= w:
        parcial.append(elementos[indice])
        peso_parcial += elementos[indice][0]
        valor_parcial += elementos[indice][1]
        sol, valor_solucion, peso_sol = mochila_bt(elementos, k, w , indice+1, parcial, sol, peso_parcial, peso_sol, valor_parcial, valor_solucion)
        parcial.pop()
        peso_parcial -= elementos[indice][0]
        valor_parcial -= elementos[indice][0]
    
    sol, valor_solucion, peso_sol = mochila_bt(elementos, k, w , indice+1, parcial, sol, peso_parcial, peso_sol, valor_parcial, valor_solucion)
    return sol, valor_solucion, peso_sol

def mochila(elementos, k, w):
    parcial = []
    sol = []
    indice = 0
    peso_parcial = 0
    peso_sol = 0
    valor_parcial = 0
    valor_solucion = 0

    return mochila_bt(elementos, k, w, indice, parcial, sol, peso_parcial, peso_sol, valor_parcial, valor_solucion)