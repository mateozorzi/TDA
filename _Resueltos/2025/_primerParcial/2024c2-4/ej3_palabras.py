"""
Queremos determinar si un texto ininteligible, sin espacios, es en realidad un texto de un idioma, al que se le borraron los espacios
(por ejemplo, "holaquehaces"). Contamos con un conjunto de las k palabras (muy cortas) del idioma en cuestión.
Implementar un algoritmo que, utilizando programación dinámica, reciba el texto, y el conjunto de palabras del idioma, y determine si,
en efecto, se trata de un texto del idioma, sin los espacios. Por ejemplo, para "argentinacampeon" debe devolver true, mientras que
para "awanteboke" debe devolver false. La resolución de este ejercicio puede ser similar a la resolución del TP2 (curso regular)/Parte
II (cursos anual y asincrónico). El ejercicio puede resolverse incluso de una forma mejor (que a algunos puede resultarles más simple).
Indicar y justificar la complejidad del algoritmo implementado
"""

def buscarOptimos(texto, diccionario):
    optimos = [False] * (len(texto)+1)
    optimos[0] = True

    #caso base, palabra de un caracter
    optimos[1] = True if texto[0] in diccionario else False

    #Tengo un texto, con palabras de un diccionario sin esapcio, y tengo que comoprobar si se forma una oracion con paplabras que estan en el diccionario
    #si no encuentro un oracion que utilice el texto y forme palabras del diccionario (sin dejar ninguna letra sin usar) entonces no es un texto
    #Al leer el paso i:j estoy leyendo del carcater i al j, si aqui hay una palabra y el optimo de el texto hasta i es True

    #opt[j] = True if texto[i:j] in diccionario and opt[i] == True else False

    for j in range(2,len(optimos)):
        for i in range(1,j+1):
            aux = texto[i-1:j]
            if optimos[i-1] and texto[i-1:j] in diccionario:
                optimos[j] = True
                break
    
    return optimos

def palabras(texto, diccionario):
    optimos = buscarOptimos(texto, diccionario)

    return optimos[-1]


texto = "holaquehaces"
dicc = {"hola", "que", "haces"}
print(palabras(texto, dicc))