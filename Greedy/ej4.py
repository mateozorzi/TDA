"""Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado."""
def charlas(horarios):
    if(len(horarios) == 0):
        return []
    horariosOrdenados = sorted(horarios, key=lambda x: x[1])
    horariosConfirmados = []
    horariosConfirmados.append(horariosOrdenados[0])
    for i in range(1,len(horariosOrdenados)):
        finalCharlaConfirmada = horariosConfirmados[-1][1]
        inicioCharlaSupesta = horariosOrdenados[i][0]
        if(inicioCharlaSupesta >= finalCharlaConfirmada):
            horariosConfirmados.append(horariosOrdenados[i])
    
    print(horariosOrdenados)
    print(horariosConfirmados)
    
    return horariosConfirmados

horarios = [(1,4),(2,3),(4,9),(5,8),(4,5),(6,9)]
charlas(horarios)