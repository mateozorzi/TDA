"""
Problema del submarino es NP-C?

subamrino: dado una matriz, con n subamrinos, se quieren colocar a lo sumo k faros dado que todos los subamrinos
queden iluminados. Cada faro iluina los adyacentes en un radio de 2 celdas (incluyendo digonales) 

1. verificado polinomial, verifico que esta en NP
2. Para verificar que sea NP-C, debo poder reducir un problema NP-C al problema del submarino

Reduccion con dominating set
HS(A,B,k) <=p submarinos(matriz, k)

HS: Dado los elementos de A, se crean subconjuntos Bi que pertenecen a A. Existe un subconjunto C de a lo sumo tamaño k, 
dado que tiene por lo menos un elemento de cada Bi

Para realizar la reduccion, creo una matriz a partir de los elementos de A, que serian todos los casilleros posibles. Luego cada Bi simbolizaria 
las casillas adyacentes a cada barco. El valor de k se mantendria. Al pasar por la caja negra que resuelv el
problema del submarino, este devolvera el subconjunto C de a los umo tamaño k, donde se ubicarian los faros que iluminan
todos los barcos.

Si hay HS, hay subamrinos.
Si hay un HS que de un subconjunto de a lo sumo tamaño k. Entonces exisitira una combinacion de faros en la matriz
donde se puedan ubicar los faros y asi iluminar todos los barcos de la matriz. Dado que cada subconjunto Bi representa
las casillas adyacentes a los barcos, si en el conjunto C hay al menos un elemento de cada Bi, entonces todos los barcos seran iluminados, ninguno quedara a oscuras.

Si hay subamrinos, hay HS
En esta instancia del problema, si existen a los sumo k faros dado que iluminen todos los barcos de la matriz. Entonces
en el problema de HS se encontrara un subconjunto C de a lo sumo k elemetnos, que represente las piscones de los faros,
que iluminaran cada barco Bi.Estas posiciones de los barcos estaran por lo menos en alguno de los subconjutnos Bi que representan las
adyacencias de los barcos. POr lo que ningun barco no tendra una posicion adyacente en el subconjunto C.

"""

def validador(matriz, faros, k, n, iluminados):
    #si hay mas faros de los esperados, no es valido 
    if len(faros) > k:
        return False
    
    #veo los submarinos iluminados
    for faro in faros:
        x = faro[0]
        y = faro[1]    
        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                if i >= 0 and i < n and j >= 0 and j < n:
                    if matriz[i][j] == 1 and (i,j) not in iluminados:
                        iluminados.add((i,j))
    
    #si la cantidad de iluminados no es la cantidad de subamrinos, no es valido
    if len(iluminados) != n:
        return False

    return True