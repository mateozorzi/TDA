"""
En su tiempo libre, Carlitos colecciona figuritas del mundial. 
Incluso a más de un año de la coronación de gloria, hay mucho entusiasmo por estas. 
Llegó a coleccionar tantas que ahora se dedica a revenderlas 
(para sacar unos pesos extra de su trabajo principal como publicista). 
Tiene tantas figuritas que ya no revende al público directamente, 
sino a otros revendedores y cadenas de kioscos. En general, 
cuando le piden, le pide un lote de figuritas “por una cantidad determinada de dinero”. 
Cada tipo de figurita tiene un valor diferente 
(es decir, la de Messi no vale lo mismo que la del Bobo Weghorst). 
Podemos decir que absolutamente todos los tipos de figuritas tienen valores diferentes, 
todos valores enteros, y que Carlitos cuenta 
con una cantidad ridículamente alta de cada una de ellas. Por un análisis que hizo, 
sabe que si le piden figuritas por un determinado monto, 
le conviene dar la menor cantidad de figuritas posibles 
(siempre cumpliendo con el monto exacto pedido), 
incluso repitiendo figuritas en caso de ser necesario. 
El problema de las figuritas de Carlitos dice: 
dados los valores de los diferentes tipos de figuritas y un monto al que llegar, 
determinar cuáles figuritas debe dar Carlitos para cumplir exactamente con dicho monto 
dando la mínima cantidad de figuritas para ello. Asumir todos valores enteros, 
y que hay figurita de valor 1. 
Por otro lado, recordemos que el Problema de SubsetSum es NP-Completo. 
Redefinir ambos problemas en sus versiones de problema de decisión, 
y realizar una reducción polinomial de uno a otro. 
¿Podemos con esta reducción afirmar que el problema de Carlitos es NP-Completo?
"""

"""
Son NP? si -> validaro polinomial

carlitos(figuritas, W, k) -> 
"Dados una serie de valores de figuritas (que se pueden repetir todas las veces que quieras), 
un monto a cumplir y un k, 
¿existe una forma de dar figuritas que cumpla exactamente con 
el monto y la cantidad de figuritas sea <= k?"

subSetSum(elementos, W, k) -> subarreglo que hace a la suma igual a W y de tamaño <= k
NP-C

Reduzco:
carlitos <=p subsetSum
No puedo reducir al reves
Esta reduccion no demuestra que el problema de carlitos sea NP-C

Transformo el arreglo de las figuritas, como subset sum no puede repetir numeros
si estan uns sola vez en el arreglo, lo que hago es agregar para cada figurita la cantidad que necesito
para llegar a o no pasarse de W, si tengo la figurita que vale 1 y W= 10, en el nuevo arreglo habra 10 veces 1, para que
subset sum pueda tener en cuenta la suma de las 10 figuritas de valor 1
Para la figurita de valor 3, habra 3 veces en el nuevo arreglo

"""