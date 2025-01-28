def parte_entera_raiz(n):
    aprox = 0
    inicio = 0
    fin = (n//2) + 1
    while inicio <= fin:
        mitad = (inicio + fin) // 2
        if(mitad**2 <= n and (mitad+1)**2 > n):
            return mitad
        elif(mitad**2 >= n):
            fin = mitad - 1

        else:
            inicio = mitad + 1

    return fin


aproximacion = parte_entera_raiz(25)
print(aproximacion)