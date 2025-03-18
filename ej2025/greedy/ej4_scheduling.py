"""

Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado.
"""

def charlas(horarios):
    if len(horarios) == 0:
        return []
    horarios = sorted(horarios, key=lambda x: x[1]) #ordeno por finalizaicon de la charla

    aceptadas = []
    aceptadas.append(horarios[0])

    for i in range(1, len(horarios)):
        charla_anterior = aceptadas[-1]
        charla_actual = horarios[i]

        if charla_anterior[1] < charla_actual[0]:
            aceptadas.append(charla_actual)
    
    
    return aceptadas
#Regla greedy: En mi situacion actual, busco agregar a la charlas aceptadas, la que antes finalice y no se superponga con las ya aecptadas
#Asi, al agregar las charlas que antes finalicen, maximizo el total de horarios libres para las sigueintes charlas.
#Es optimo ya que agregare las charlas que antes finalicen y no se pisen entre si, el tiempo entre charlas aceptadas sera optimo y aceptare la mayor cantidad de charlas
#Complejidad: O(n)
