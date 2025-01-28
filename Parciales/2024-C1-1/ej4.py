def potencia(b, n): #b^n
    if n == 0:
        return 1
    if n == 1:
        return b
    
    if n % 2 == 0:
        num = potencia(b, n/2)
        return num*num
    else:
        num = potencia(b, (n-1)/2)
        return b*num*num


print(potencia(5,10))