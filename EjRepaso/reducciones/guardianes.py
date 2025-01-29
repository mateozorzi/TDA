"""
Guardianes = ¿Se pueden vigilar todas las calles con esta topología con al lo sumo K guardianes?

1. Verifico que que sea NP con un validador polinomial

2. Reduzco un problema NP-C al problema de los guardianes

VC(grafo, k) <=p guardianes(ciudad,k)



"""

def validador(ciudad, cuadras, k, guardianes):
    esquinas = set(cuadras)
    guardianes = set(guardianes)
    if len(guardianes) > k:
        return False
    
    for guardia in guardianes: #O(k)
        if guardia not in esquinas: #O(1)
            return False
    
    for cuadra in esquinas: #O(n)
        for ady in ciudad.adyacentes(cuadra): #O(n)
            if cuadra not in guardianes and ady not in guardianes: #O(1)
                return False
    
    return True

#complejidad O(n^2) es polinomial