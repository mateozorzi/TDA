"""
Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, 
utilizando programación dinámica, permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. 
El algoritmo debe devolver el valor del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10. 
Indicar y justificar la complejidad del algoritmo.

Ejemplos:

n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
n = 4 --> Debe devolver 4 (producto máximo es 2 * 2)
n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
n = 6 --> Debe devolver 9 (producto máximo es 3 * 3)
n = 7 --> Debe devolver 12 (producto máximo es 3 * 4)
n = 10 --> Debe devolver 36 (producto máximo es 3 * 3 * 4)
"""

#ec de recurrencia:
# Tengo un soga que debo cortar al menos vez por l0 menos y me debo quedar con el maximo producto de sus cortes.
# Por lo que puedo hacer un corte entre 1 y largo-1 de la soga. Al cortar la soga tengo dos opciones,
# sigo cortandola o no, tengo que ver que me conviene con los optiomos que calcule anteriormente.
# Para esto me quedare con el mayor producto que me de multicplicar pór el optimo de la soga restante o el rtesto de la soga sin cortar
# Ec de recu -> optimos[i] = max(   optimos[i]          ,          j   *            max(optimos[i-j], i-j))
#                               Optimo actual de la soga,       donde hago              eligo entre cortar la soga restante nuevamente
#                                                               el primer               o no la corto mas
#                                                               corte de la soga
# Para cada largo de la soga hare varias iteraciones por cada corte que puedo hacer, hasta quedarme con el maximo

#compejidad del algortimo es O(n^2), siendo n el largo de la soga

def buscarOptimos(n):
    optimos = [0] * (n+1)
    optimos[0] = 0
    optimos[1] = 1

    for i in range(2,len(optimos)):
        for j in range(1,i):
            optimos[i] = max(optimos[i], j * max(optimos[i-j], i-j))

    return optimos

def reconstruccion(n, optimos, pos):
    sol = []

    while pos > 0:
        for j in range(pos-1,0,-1):
            if j * optimos[pos-j] == optimos[pos]:
                sol.append(j)
                pos -= j
                break
            elif j * (pos-j) == optimos[pos]:
                sol.append(j)
                sol.append(pos-j)

                pos -= (pos-j) + j
                break

    return sol

def problema_soga(n):
    
    optimos = buscarOptimos(n)

    return optimos[-1]
    

n = 10
print(problema_soga(n))