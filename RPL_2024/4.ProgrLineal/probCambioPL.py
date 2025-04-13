"""
Var:
Creo variables binaria para cada tipo de cambio que tengo

Restricciones:
la suma de las variables por la cantidad de uso no puede ser mayor al cambio a dar


Funcion Objetivo:
la sumatoria de la cantidad de distitno cambio a dar debe ser minima,
es decir tengo que minimizar el uso de las monedas
min sumatoria de ci

"""
import grafo
import pulp



def cambioPL(monedas, cambio):
    v = []
    for i in range(len(monedas)):
        v.append(pulp.LpVariable("v" + str(i), cat="Integer", lowBound=0)) #Creo las variables
    
    problem = pulp.LpProblem("Cambio", pulp.LpMinimize)
    problem += pulp.LpAffineExpression({v[i]: monedas[i] for i in range(len(monedas))}) == cambio
    problem += pulp.LpAffineExpression([(v[i],1) for i in range(len(v))])
    problem.solve()

    return [pulp.value(vi) for vi in v]


ej1 = [13,9,7,2,1]
print(cambioPL(ej1,16))