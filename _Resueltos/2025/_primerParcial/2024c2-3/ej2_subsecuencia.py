"""
Resolver el problema anterior, pero esta vez para encontrar el largo de la subsecuencia balanceada más larga de
una expresión (en este caso, no necesariamente comenzando en el inicio). Para esto, utilizar programación dinámica. La
solución a este problema no dista mucho al planteo de la parte 2 del TP. Escribir y describir la ecuación de recurrencia
de la solución, e indicar y justificar la complejidad del algoritmo implementado
Ejemplo: para ()())(())()(() la respuesta es 6 (comenzando en la posición 5)
"""

def buscarOptimos(cadena):
    optimos = [[0] * (len(cadena)+1) for _ in range(len(cadena)+1)]
    #ec de recurrencia -> las filas seran el indice en donde empieza mi subproblema en la cadena,
    #mientras que las columnas seran el indice de fin.
    #Enonces yo puedo ver que si el caracter en el inicio es ( y el caracter en el fin es ), y el largo optimo para el subporblema
    #optimos[i+1][j-1] tiene largo (j-1)-(i+1), es decir todos los caracters intermedios, entonces desde incio a fin sera una subsecuencia valida
    #si el inicio stiene uin caracter de cierre y el fin de cierre tambien me quedo con subproblema sin contar estos
    #lo mismo si el inicio tiene de apertura y el fin de apertura, o si el inicio de cirre y el fin de apertura

    #casos base:
    #las col no pueden ser mayores que las filas, opt[i][j] = 0
    #si hay un solo caracter, inicio = fin, no puede estar balanceada, opt[i][j] = 0
    abrir = "("
    cerrar = ")"
    for i in range(len(optimos)-1,-1,-1):
        for j in range(i, len(optimos[0])):
            if i == 5 and j == 10:
                pass
            if i == j:
                continue

            if cadena[i] == abrir and cadena[j] == cerrar:
                if optimos[i+1][j-1] == (j) - (i+1):
                    optimos[i][j] = 2 + optimos[i+1][j-1]
                else:
                    optimos[i][j] = optimos[i+1][j-1]

            else:
                optimos[i][j] = optimos[i+1][j-1]

    return optimos


            
def subsecuencia_mas_larga(cadena):
    optimos = buscarOptimos(cadena)

    return optimos[-1][-1]


c = "()())(())()(()"
print(subsecuencia_mas_larga(c))
