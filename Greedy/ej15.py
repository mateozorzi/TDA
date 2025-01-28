"""Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros). 
Tu objetivo es guardar esos libros en la menor cantidad de cajas. 
Todas las cajas disponibles son de la misma capacidad L (se asegura que L >= n). Obviamente, 
no podés partir un libro para que vaya en múltiples cajas, pero sí podés poner múltiples libros en una misma caja, 
siempre y cuando los espesores no superen esa capacidad L. 
Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar. 
Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. 
¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.

¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros? Describir cómo afecta a la complejidad,y a su optimalidad."""

def cajas(capacidad, libros):
    if(len(libros) == 0):
        return []
    libros = sorted(libros)

    cajas = []

    indice = 0
    while(indice < len(libros)):
        caja = []       
        while(indice < len(libros) and sum(caja) + libros[indice] <= capacidad):
            caja.append(libros[indice])
            indice += 1
        if(indice < len(libros) and libros[indice] > capacidad):
            indice += 1

        if(caja):
            cajas.append(caja)
    
    
    return cajas

libros = [4, 2, 1, 3, 5]
print(cajas(7,[3, 3, 2, 2, 2, 2]))