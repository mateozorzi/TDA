"""
Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El algoritmo debe devolver el valor del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10. Indicar y justificar la complejidad del algoritmo.

Ejemplos:

n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
n = 4 --> Debe devolver 4 (producto máximo es 2 * 2)
n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
n = 6 --> Debe devolver 9 (producto máximo es 3 * 3)
n = 7 --> Debe devolver 12 (producto máximo es 3 * 4)
n = 10 --> Debe devolver 36 (producto máximo es 3 * 3 * 4)
"""

#recurrencia -> opt[n] = max (  )

def calculoOptimos(n):
    optimos = [0] * (n+1)
    optimos[1] = 1

    for i in range(2,len(optimos)):
        for j in range(1, i):
            optimos[i] = max(optimos[i], max(j, optimos[j]) * max(i-j, optimos[i-j]))
                            #Corto la soga ne la pos j, y consigo los poptimos de las mitades que quedan. Veo si
                            #me conviene seguir cortando o me quedo con ese trozo de soga
    return optimos



def problema_soga(n):
    if n < 2:
        return 0
    
    optimos = calculoOptimos(n)
    
    return optimos[-1]


# Ejemplos de uso
"""print(problema_soga(2))  # Devuelve 1
print(problema_soga(3))  # Devuelve 2
print(problema_soga(4))  # Devuelve 4
print(problema_soga(5))  # Devuelve 6
print(problema_soga(6))  # Devuelve 9
print(problema_soga(7))  # Devuelve 12"""
print(problema_soga(10))  # Devuelve 36