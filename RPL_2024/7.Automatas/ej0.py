from automata import Automata

def automata_al_menos_3_0s():
    a = Automata()
    a.estado("q0", es_inicial=True)
    a.estado("q1")
    a.estado("q2")
    a.estado("q3", es_final=True)

    a.transicion_estado("q0","q1","0")
    a.transicion_estado("q0","q0","1")
    a.transicion_estado("q1","q2","0")
    a.transicion_estado("q1","q0","1")
    a.transicion_estado("q2","q3","0")
    a.transicion_estado("q2","q0","1")
    a.transicion_estado("q3","q3","0")
    a.transicion_estado("q3","q0","1")

    return a