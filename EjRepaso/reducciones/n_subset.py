"""
Dado un número n, encontrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados.
Reduccion con subset sum es NP-C

1. validador para probar que el problema es NP
2. Reduccion a subsetSum

Dada esta reduccion, no podemos comprobar si n^2_subset es NP-C, dado que ya sabemos que subsetSUm es NP-C, por lo que
nuestro porblema sera como mucho igual de dificil que subsetSUm, pero no afirmaria que sea NP-C
Reduccion:
n_subset <=p subsetSum(numeros, n)

Para realizar esta reduccion, dado un array de numeros, elevamos todos estos al cuadrado y se lo pasamos
a la caja negra que resuelve subsetSum. Recibiremos los terminos que dan la suma de n y para luego saber que numeros
al cuadrado son el resultado se le aplica raiz cuadrada a cada termino. Conisguiendo asi la cantidad mas
economica de escribir n como suma de cuadrados.
"""

def validador(n, cuadrados, k):
    if not cuadrados:
        return False
    if len(cuadrados) > k:
        return False
    suma = 0
    for i in range(len(cuadrados)):
        suma += cuadrados[i]**2
        if suma > n:
            return False
    
    if suma != n:
        return False
    
    return True