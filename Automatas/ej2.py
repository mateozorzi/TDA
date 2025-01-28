'''
Implementar un Autómata Finito Determinista que describa al Lenguaje que acepta todos las cadenas de 0 y 1s tales que tienen una cantidad par tanto de 0s como de 1s.
'''
from automata import Automata

def automata_pares_1y0():
    a = Automata()
    a.estado("q0", es_inicial=True, es_final=True)  # #0 par y #1 par
    a.estado("q1")                                  # #0 imapr y #1 par 
    a.estado("q2")                                  # #0 par y #1 impar
    a.estado("q3")                                  # #0 impar y #1 impar

    a.transicion_estado("q0", "q1", "0")
    a.transicion_estado("q0", "q2", "1")
    a.transicion_estado("q1", "q0", "0")
    a.transicion_estado("q1", "q3", "1")
    a.transicion_estado("q2", "q3", "0")
    a.transicion_estado("q2", "q0", "1")
    a.transicion_estado("q3", "q2", "0")
    a.transicion_estado("q3", "q1", "1")
      
    # resolucion del ejercicio
    return a