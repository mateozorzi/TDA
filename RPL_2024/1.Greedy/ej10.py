"""Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.
Ejemplo:

| Ciudad      | Bifurcación |
|-------------|-------------|
| Castelli    | 185         |
| Gral Guido  | 242         |
| Lezama      | 156         |
| Maipú       | 270         |
| Sevigne     | 194         |
Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.
En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne."""

def bifurcaciones_con_patrulla(ciudades):
    if(len(ciudades) == 0):
        return []
    ciudadesOrdenadoPorKm = sorted(ciudades, key=lambda x: x[1])

    cantCiudadesCubiertas = []
    for ciudad in ciudadesOrdenadoPorKm:
        aux = []
        cantCubiertas = 0
        ciudadesCubiertas = []
        for otraCiudad in ciudadesOrdenadoPorKm:
            if(abs(otraCiudad[1] - ciudad[1]) <= 50 and otraCiudad[1] - ciudad[1] != 0):
                cantCubiertas += 1
                ciudadesCubiertas.append(otraCiudad)
        aux.append(ciudad[0])
        aux.append(ciudad[1])
        aux.append(cantCubiertas)
        aux.append(ciudadesCubiertas)
        cantCiudadesCubiertas.append(aux)
                

    cantCiudadesCubiertas = sorted(cantCiudadesCubiertas, key=lambda x:x[2],reverse=True)

    ciudadesConVigilancia = []
    ciudadesConCobertura = []
    for ciudad in cantCiudadesCubiertas:
        #ciudad = [ciudad[0], ciudad[1]]
        if((ciudad[0], ciudad[1]) not in ciudadesConVigilancia and (ciudad[0], ciudad[1]) not in ciudadesConCobertura):
            ciudadesConVigilancia.append((ciudad[0], ciudad[1]))
            for ciudadesCubiertas in ciudad[3]:
                ciudadesConCobertura.append((ciudadesCubiertas[0], ciudadesCubiertas[1]))

        
    return ciudadesConVigilancia

ciu = [("Castelli", 185), ("Gral Guido", 242), ("Lezama", 156), ("Maipu", 270), ("Sevigne", 194)]
#print(bifurcaciones_con_patrulla(ciu))

ciu = [("Castelli", 185), ("Gral Guido", 242), ("Sevigne", 194)]
#print(bifurcaciones_con_patrulla(ciu))

ciu = [("Castelli", 100), ("Gral Guido", 150), ("Sevigne", 50)]
#print(bifurcaciones_con_patrulla(ciu))

ciu = [('d', 801), ('a', 51), ('c', 149), ('f', 899), ('b', 100), ('e', 850)]
#print(bifurcaciones_con_patrulla(ciu))

ciu = [('a', 0), ('b', 30), ('d', 90), ('e', 120), ('c', 60)]
print(bifurcaciones_con_patrulla(ciu))
