"""
Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1^2, por lo que siempre existe solución.
Sin embargo, la expresión 10 = 3^2+ 1^2 es una manera más económica de escribirlo para n= 10, pues sólo tiene dos
términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
necesaria
"""

def buscarOptimos(n):
    optimos = [0] * (n+1)

    optimos[0] = 0
    for j in range(1,len(optimos)):
        optimos[j] = j

    optimos[1] = 1

    #ec de recurrencia: tengo que buscar la minima cantidad de termino para representar a n como una suma de cuadrados. Para esto tengo que buscar los numeros 
    #mas optimos a sumar en una suma de cuadrados tal que me minimicen la cantidad de terminos. 
    #puedo fijarme en los numeros desde 1 a k, siendo k el numero donde (k+1)^2 > n, entonces no me sirve para hacer la suma de cuadrados.
    #con estos numeros de 1 a k, me dijo ne mis solucines optimas ya calculadas cual es su optimo y que quedare con el que tenga menos terminos

    #ec de recurencia -> optimos[i] = min(      optimos[i]           ,      optimos[i - k**2] + 1)
    #                                       optimo antes calculado   ,      encuentro un k, que la potencia en menor a i y veo cual es la cantidad minima de termino que lo puedo escirbir y le sumo 1

    for i in range(2, len(optimos)):
        k = 1
        while k**2 <= i:
            optimos[i] = min(optimos[i], optimos[i-k**2] + 1)
            k+=1
    
    return optimos

def reconstruccion(n, optimos, pos):
    sol = []


    while pos > 0:
        k = 1

        while k**2 <= pos:
            optimos_menos_k = optimos[pos-k**2]

            if optimos_menos_k + 1 == optimos[pos]:
                break
        
            k += 1

        sol.append(k)
        pos -= k**2

    return sol

def suma_cuadrados(n):
    optimos = buscarOptimos(n)
    return reconstruccion(n, optimos, len(optimos)-1)

n = 745
print(suma_cuadrados(n))

