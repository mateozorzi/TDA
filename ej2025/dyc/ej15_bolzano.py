"""
Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. Justificar la complejidad de la función implementada.
"""

def raiz(funcion, a, b):
    #busco un punto C en la mitad de a y b
    c = (a + b) // 2

    fa = funcion(a)
    fb = funcion(b)
    fc = funcion(c)

    if fc == 0:
        return c
    
    if fa > 0 and fc > 0:
        #la raiz estara entre c y b
        return raiz(funcion,c,b)
    elif fa > 0 and fc < 0:
        #la raiz estara entre a y c
        return raiz(funcion,a,c)
    
    elif fa < 0 and fc < 0:
        #estara entre c y b
        return raiz(funcion,c,b)
    elif fa < 0 and fc > 0:
        #estara entre a y c
        return raiz(funcion,a,c)
    
#complejidad:
#T(n) = T(n/2) + O(1) -> por TM -> A = 1, B = 2, C = 0 -> log b(A) = 0 = C -> O(n^c logB(A)) = O(logn)
    