def potencia(b,n):
    #Por TM, para tener complejidad O(logn)
    #A = 1
    #B = 2
    #C = 1
    # log2 (1) = 1 = 1 = C
    if n == 0:
        return 1
    if n == 1:
        return b
    
    if n % 2 == 0:
        #exponente par
        mitad = n//2
        t1 = potencia(b,mitad)
        return t1 * t1
    else:
        #exponente impar
        mitad = n // 2
        t1 = potencia(b, mitad)
        return t1 * t1 * b
    

b = 2
n = 10
print(potencia(b,n))

