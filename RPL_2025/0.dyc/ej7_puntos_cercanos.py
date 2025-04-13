"""
Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con un orden de complejidad mejor que O(n^2). Justificar la complejidad del algoritmo mediante el teorema maestro.
"""

def dist(punto1, punto2):
    return (abs(punto1[0] - punto2[0])**2 + abs(punto1[1] - punto2[1])**2 ) **(0.5)

def dividir_puntos_y(Py, x_limite):
    Qy = []
    Ry = []

    for punto in Py:
        if punto[0] < x_limite:
            Qy.append(punto)
        else:
            Ry.append(punto)

    return Qy, Ry


def construir_Sy(Py, x_limite, d_min):
    Sy = []

    for punto in Py:
        if abs(punto[0] - x_limite) < d_min:
            Sy.append(punto)
    
    return Sy

def puntos_cercanos_dyc(Px, Py):
    #casos base -> tengo dos puntos o tengo 3 puntos
    if len(Px) == 2:
        return Px[0], Px[1]
    if len(Px) == 3:
        d1 = dist(Px[0], Px[1])
        d2 = dist(Px[1], Px[2])
        d3 = dist(Px[0], Px[2])

        if d1 < d2 and d1 < d3:
            return Px[0], Px[1]
        elif d2 < d3:
            return Px[1], Px[2]
        else:
            return Px[0], Px[2]
    
    #divido el plano e dos mitades
    mitad = len(Px) // 2
    x_limite = Px[mitad][0]
    #creo conjunhtos para los puntos a la izq y los puntos a la derecha

    Qx = Px[:mitad]
    Rx = Px[mitad:]

    #para los puntos en y, tambien lo divido segun el x_limite
    Qy, Ry = dividir_puntos_y(Py, x_limite)

    #resuelvo los subproblemas
    q1,q2 = puntos_cercanos_dyc(Qx, Qy)
    dq = dist(q1,q2)

    r1, r2 = puntos_cercanos_dyc(Rx, Ry)
    dr = dist(r1,r2)

    d_min = 0
    p1 = 0
    p2 = 0

    #me quedo con la menor distancia
    if dq < dr:
        d_min = dq
        p1 = q1
        p2 = q2
    else:
        d_min = dr
        p1 = r1
        p2 = r2
    
    #que pasa en el limite de la particion? Tengo que ver si hay dos puntos que estan cerca, pero separados por x_limite
    #Contruyo Sy con los puntos que estan a lo sumo a d_min de x_limite

    Sy = construir_Sy(Py, x_limite, d_min)

    for i in range(len(Sy)):
        for j in range(i+1, min(len(Sy), i+15)):
            if dist(Sy[i], Sy[j]) < d_min:
                d_min = dist(Sy[i], Sy[j])
                p1 = Sy[i]
                p2 = Sy[j]
    
    return p1, p2



def puntos_mas_cercanos(puntos):
    Px = sorted(puntos, key=lambda x: x[0])
    Py = sorted(puntos, key=lambda x: x[1])

    p1,p2 = puntos_cercanos_dyc(Px, Py)

    sol = []

    sol.append(p1)
    sol.append(p2)

    return sol

puntos = [(0, 10), (1, 1), (2, 2), (3, 4)]
print(puntos_mas_cercanos(puntos))