'''
Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular:
(aab)*(a, aba)*

Como recordatorio:

El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.
Esta expresión acepta todas las cadenas que tengan una cantidad indefinida de aab como inicio, luego puedan tener una cantidad indefinida de a o aba (que pueden estar intercaladas).
'''

from automata import Automata

def expresion():
    a = Automata()
    a.estado("-",es_inicial=True, es_final=True)
    a.estado("a1")
    a.estado("a2")
    a.estado("a3", es_final=True)
    a.estado("b", es_final=True)
    a.estado("b2")

    a.transicion_estado("-","a1","a")
    a.transicion_estado("-","a3","a")
    a.transicion_estado("a1","a2","a")
    a.transicion_estado("a2","b","b")
    a.transicion_estado("a2","b","")
    a.transicion_estado("b","a1","a")
    a.transicion_estado("b","a3","a")
    #a.transicion_estado("b","a3","")
    a.transicion_estado("a3","a3","a")
    a.transicion_estado("a3","b2","b")
    a.transicion_estado("b2","a3","a")



    # resolucion del ejercicio
    return a

