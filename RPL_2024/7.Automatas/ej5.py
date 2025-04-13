'''
Implementar un Autómata Finito No Determinista que acepte las cadenas que cumplan con la expresión regular:
((ab)+ba*)?(b*(ab)*)

Notar que la expresión es equivalente a:
((ab)+ba*)?b*(ab)*

Como recordatorio:

El símbolo + indica que el símbolo anterior (o grupo, si está entre paréntesis) aparece al menos una vez (puede aparecer muchas veces, de forma contigua).
El símbolo ? indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer una vez, o no estar (es decir, es opcional).
El símbolo * indica que el símbolo anterior (o grupo, si está entre paréntesis) puede aparecer tantas veces como sea (puede ser ninguna o muchas) de forma contigua.
'''
from automata import Automata

def expresion():
    a = Automata()
    a.estado("-", es_inicial=True, es_final=True)
    a.estado("a")
    a.estado("b")
    a.estado("b1")
    a.estado("a1", es_final=True)
    a.estado("b2", es_final=True)
    a.estado("a2")
    a.estado("b3", es_final=True)

    a.transicion_estado("-","a","a")
    a.transicion_estado("-","b2","b")
    a.transicion_estado("-","b2","")
    a.transicion_estado("a","b","b")
    a.transicion_estado("b","a","a")
    a.transicion_estado("b","b1","b")
    a.transicion_estado("b1","a1","a")
    a.transicion_estado("b1","a1","")
    a.transicion_estado("a1","a1","a")
    a.transicion_estado("a1","b2","b")
    a.transicion_estado("a1","b2","")
    a.transicion_estado("b2","b2","b")
    a.transicion_estado("b2","a2","a")
    a.transicion_estado("b2","a2","")
    a.transicion_estado("a2","b3","b")
    a.transicion_estado("b3","a2","a")


    return a