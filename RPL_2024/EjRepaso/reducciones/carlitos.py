"""
Podremos asumir que el problema de carlitos es NP-C si

Carlitos = dados los valores de los diferentes tipos de figuritas y un monto al que llegar, 
determinar cuáles figuritas debe dar Carlitos para cumplir exactamente con dicho monto 
dando la mínima cantidad de figuritas para ello.
Asumir todos valores enteros, y que hay figurita de valor 1.
La cantidad de figuritas dada sera de a lo sumo k.

SubsetSum = dado una lista de numeros y un valor n, cual sera la cantidad minima de nuemeros, que sumados den n. y de tamaño a lo sumo k

1. validador polinomial de una solucion al problema
2. Reducir un problema NP-C, como subsetSum, al problema de carlitos

subsetSum(numeros, valor, k) <= p carlitos(figuritas, valor, k)
No puedo reducir de esta manera

carlitos <=p subsetSum
Esta reduccion no afirma que el problema de carlito es NP-C


"""