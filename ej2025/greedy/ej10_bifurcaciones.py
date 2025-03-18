"""
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
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
En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.
"""

def bifurcaciones_con_patrulla(ciudades):
    if len(ciudades) == 0:
        return []
    
    ciudades = sorted(ciudades, key=lambda x:x) #ordeno por el km donde este

    cubierto = 0
    estaciones = []

    for i in range(len(ciudades)):
        if ciudades[i] > cubierto:
            cubierto = ciudades[i] + 50
            estaciones.append(ciudades[i])
    
    return estaciones

#Regla greddy: En mi situacion actual, veo si la ciudad esta cubierta por las estaciones policiales colocadas anteriuoremente, si no lo esta pongo una estacion
#esta estacion tambien cubirira 50km hacia adelante, si alguna ciudad se encuntra en ese rango no colocare otra estacion
#Es optimo ya que al tener en cuenta hasta que km esta cuibierto por la estacion anterior, puedo ahorrar de colocar una estaciuon en una ciudad que este en un rango de 50km
#con alguna anterior