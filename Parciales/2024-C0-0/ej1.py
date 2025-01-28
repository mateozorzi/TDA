"""
Problemas de desicion:
2-Partition: "Dado un conjunto de n elementos, cada uno con un valor asociado.
            Se desea separar en 2 subconjuntos, tal que la suma de ambos por separado sea k"
SubsetSum: "Dado un arreglo n de elementos, existe una suma entre estos que de igual k' "

2-Partition en NP-Completo
validador para que subsetSUm es NP.

Quiero reducir 
2-Partition <=p SubsetSum

Para la reduccion, primero calculo la suma total que dan los valores de los elementos K,
por lo que para que ambos subconjuntos den iguales, deberia corroborar si existe un subconjunto que de como suma K/2 = k'
Utitlizo mi caja negra que resuelve subsetSum, para ver si con los elementos, ecncutra un subconjunto que suma k'
Si devuelve True, pues podre crear 2 subconjuntos que sus sumas sean iguales. Por lo que
cumplire con 2-Partition

Si hay SubSetSum, hay un 2-Partiton valido?
Si existe un subconjunto de los elementos, tal que la suma da con la transformacion k'. 
Dado que k' lo definimos igual a K/2, existiran dos subconjuntos dado que su suma es igual a k'

si y solo si
Si hay un 2-Partition, hay un subsetSum valido?
Si para un conjunto de elementos n aribitrario existe un 2-Partiton, dado que la suma de los conjntos
por separado da k'. Implica que cada uno de estos conjuntos es un subset sum del arreglo original, tambien de suma igual a k'


"""

def validadorSubSetSum(elementos, k ,solucion):
    for s in solucion:
        if s not in elementos:
            return False

    if sum(solucion) != k:
        return False
    
    return True