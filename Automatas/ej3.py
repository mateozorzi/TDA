import automata
def autoDet():
    a = automata.Automata()
    a.estado("q0", es_inicial=True)
    a.estado("q1")
    a.estado("q2", es_final=True)
    a.estado("q3")
    a.estado("q4")
    a.estado("q5",es_final=True)

    a.transicion_estado("q0", "q1", "a")
    a.transicion_estado("q0", "q3", "b")
    a.transicion_estado("q0", "q3", "c")
    a.transicion_estado("q1", "q4", "a")
    a.transicion_estado("q1", "q5", "b")
    a.transicion_estado("q1", "q2", "c")
    a.transicion_estado("q2", "q2", "a")
    a.transicion_estado("q2", "q2", "b")
    a.transicion_estado("q2", "q2", "c")
    a.transicion_estado("q3", "q4", "a")
    a.transicion_estado("q3", "q3", "b")
    a.transicion_estado("q3", "q3", "c")
    a.transicion_estado("q4", "q4", "a")
    a.transicion_estado("q4", "q5", "b")
    a.transicion_estado("q4", "q3", "c")
    a.transicion_estado("q5", "q4", "a")
    a.transicion_estado("q5", "q3", "b")
    a.transicion_estado("q5", "q3", "c")

    #Implementar un algoritmo que "acepte" el mismo lenguaje que el siguiente 
    #Autómata Finito Determinista.
    #Es decir, implementar una función es_parte_lenguaje que reciba una cadena 
    # y devuelva True si la cadena forma del lenguaje del siguiente autómata definido en la funcion de arriba.
    #La función debe ejecutar en tiempo constante O(1). 
    #Se garantiza que la cadena solamente contiene como posibles símbolos a, b y c.
def es_parte_lenguaje(cadena): #Complejidad O(1)
    if len(cadena) <= 1:
        return False
    
    indice = 0
    
    if cadena[0:2] == 'ac':
        return True #estado q2
    
    if cadena == 'ab':
        return True

    if cadena[-1] == 'b':
        indice = len(cadena)-2 #indice en anteultimo caracter
        if cadena[indice] == 'a':
            return True
    
    return False

    '''

    if cadena[indice] == 'a':
        indice += 1
        if cadena[indice] == 'c':
            return True #estado q2
        elif cadena[indice] == 'b':
            if len(cadena) == indice + 1:
                return True #termina en estado q5 
        else: #cadena[indice] == 'a'
            indice += 1
            while cadena[indice] == 'a':
                indice += 1
            if cadena[indice] == 'b':
                if len(cadena) == indice + 1:
                    return True #termina en estado q5
            elif cadena[indice] == 'c':
                indice += 1

            
    else: #cadena[0] == 'b' o cadena[0] == 'c'
        indice += 1
        while cadena[indice] == 'b' or cadena[indice] == 'c':
            indice += 1
        if cadena[indice] == 'a':
            indice += 1
            while cadena[indice] == 'a':
                indice += 1
            if cadena[indice] == 'b':
                if len(cadena) == indice + 1:   
                    return True #estado q5

    '''

    return False
    
cadenas = ["a",

"b",

"c",

"ac",

"ab",

"acab",

"acbbccab",

"acabcacbabb",

"acabcacbbbbbbbabb",

"ababcacbabbab",

"ababcacbabba",

"ababcacbabbac",

"ababcacbabbacb",

"ababcacbababcb",

"ababcacbbbbababcb"]

rta = [False, False, False, True, True, True, True, True, True, True, False, False, False, False, False]

for cadena in cadenas:
    print(f"{cadena} -> ",es_parte_lenguaje(cadena), "rta : ", rta[cadenas.index(cadena)])