"""
Debido a la trágica situación actual, es necesario realizar tests para detectar si alguna persona está contagiada de COVID-19. El problema es que los insumos tienden a ser bastante caros, y no vivimos en un país al que los recursos le sobren.

Supongamos que por persona se toma más de una muestra (lo cual es cierto, pero a fines del ejercicio supongamos que son muchas muestras), y que podemos realizar un testeo a más de una persona al mismo tiempo mezclando las muestras (lo cual también es cierto): determinamos un conjunto de personas a testear, obtenemos una muestra de cada una de ellas, las “juntamos”, y al conjunto le realizamos el test. Si el test resulta negativo, implica que todas las personas testeadas en conjunto resultaron negativas. Si resulta positivo, implica que al menos una de las personas testedas resulta positiva.

Suponer que existe una función pcr(grupo), que devuelve true si al menos una persona del grupo es COVID-positivo, y false en caso contrario (los grupos pueden estar formados por 1 o más personas). Suponer que la positividad es extremadamente baja, e inclusive pueden suponer que va a haber una única persona contagiada (por simplicidad).

Implementar un algoritmo que dado un conjunto de n personas, devuelva la o las personas contagiadas, utilizando la menor cantidad de tests posibles (considerando la notación Big Oh). En dicha notación, ¿cuántos tests se estarán utilizando?

Pueden considerar que habrá una única persona contagiada, pero esto no cambiará el análisis a realizar.
"""

def pcr(grupo):
    if sum(grupo) >= 1:
        return True
    return False

def covid_dyc(grupo):
    if len(grupo) == 1:
        return grupo
    
    mitad = (len(grupo)-1) // 2

    izq = grupo[:mitad]
    der = grupo[mitad:]

    cont_izq = None
    cont_der = None

    if pcr(izq):
        cont_izq = covid_dyc(grupo)
    elif pcr(der):
        cont_der = covid_dyc(grupo)

    if cont_izq != None and cont_der != None:
        return cont_izq + cont_der
    
    if cont_izq != None:
        return cont_izq
    elif cont_der != None:
        return cont_der
    
    return None
    
#T(n) = T(n/2) + O(1) -> A = 1, B = 2, C = 0 -> log B(A) = 0 = C -> O(n^C logn) -> O(logn)

    
