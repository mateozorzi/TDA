"""Hacer un seguimiento de obtener el flujo máximo en la siguiente red de transporte, realizando las modificaciones previas que fueran necesarias. Luego, definir cuáles son los dos conjuntos del corte mínimo en dicha red."""

def obtener_flujo():
    flujo = {}
    vertices = "super_fuente", "S", "T", "U", "V", "W", "X", "Z"
    flujo[("super_fuente", "S")] = 7 # completar
    flujo[("super_fuente", "X")] = 2 # completar
    flujo[("S", "V")] = 4 # completar
    flujo[("S", "U")] = 3 # completar
    flujo[("V", "T")] = 3 # completar
    flujo[("V", "W")] = 1 # completar
    flujo[("W", "T")] = 6 # completar
    flujo[("U", "W")] = 4 # completar
    flujo[("X", "Z")] = 2 # completar
    flujo[("Z", "W")] = 1 # completar
    flujo[("Z", "U")] = 1 # completar
    flujo[("U", "Z")] = 0 # completar

    conjunto_super_fuente = [] # completar
    conjunto_sumidero = [] # completar

    return flujo, conjunto_super_fuente, conjunto_sumidero