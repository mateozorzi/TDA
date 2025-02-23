# guardias = (nombre,dias que comeinza a trabajar, dia que termian de trabajar)
def guardiasCampo(guardias):

    guardias = sorted(guardias, key=lambda x: x[2]-x[1], reverse=True) #ordeno por la cantidad de dias que trabajan, de mayor a menor

    diacubierto = 0
    sol = set()

    for dia in range(1,32):
        if diacubierto == 31:
            break
        if dia > diacubierto:
            for guardia in guardias:
                if guardia[0] in sol:
                    continue
                if dia >= guardia[1] and dia <= guardia[2]:
                    diacubierto= guardia[2]
                    sol.add(guardia[0])
                    break
    return sol


#regla greedy: En cada iteracion, si el dia no se encuentra cubierto, agrego al guardia que mas dias trabaje y que cubra este dia.
#Es optimo ya que en cada iteracion se agrega el guardai que mas dias cubra, actualizando el dia cubierto al dia donde deja de trabajar este, por lo que
#siempre se maximiza la cantidad de dias cubiertos.
#complejidad O(g + d) -> g la cantidad de guardias, d cantidad de dias (es cte) -> O(g)

guardias = [
    ["Hola", 10,11],
    ["Chau", 2,14],
    ["Como", 1,5],
    ["Estas", 1,2],
    ["Todo", 15,19],
    ["Bien", 20,21],
    ["Y", 22,25],
    ["Vos", 6,13],
    ["?", 26,31],
    ["Muy", 28,29],
    ["Bien", 30,31]
]
print(guardiasCampo(guardias)) #deberia devolver: ["Chau", "Todo", "Bien", "?"]

