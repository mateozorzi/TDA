"""Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, 
siendo que las operaciones posibles son:

(i) aumentar el valor del operando en 1;

(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). 
Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'"""

def invertirRecurrencia(k,pos,cantOp,operaciones):
    if pos == 0 or k == 0:
        return operaciones
    
    if k % 2 == 0:
        if cantOp[pos-1]+1 >= cantOp[pos//2]+1:
            operaciones.append("por2")
            return invertirRecurrencia(k//2,pos//2,cantOp,operaciones)
    else:
        operaciones.append("mas1")
        return invertirRecurrencia(k-1,pos-1,cantOp,operaciones)

def operaciones(k):
    if k == 0:
        return []
    #ec recurrencia ->  Par: cantOp = min(cantOp[i-1], cantOp[i//2]) + 1
    #                   Impar:cantOp = cantOp[i-1] +1

    cantOp = [0] * (k+1)
    cantOp[0] = 0
    
    for i in range(1,k+1):
        if i % 2 == 0:
            cantOp[i] = min(cantOp[i-1], cantOp[i//2]) + 1
        else:
            cantOp[i] = cantOp[i-1] + 1
    print
    operaciones = []
    invertirRecurrencia(k,k+1,cantOp,operaciones)
    operaciones = list(reversed(operaciones))

    return operaciones
#complejidad  #O(k)

#greedy, no me fijo cuando es par en i-1. Nada me impide no tener que fijarme.
def ejercicio11(k) :
    optimo = [0] * (k+1)
    for i in range(1,k + 1):
        if i % 2 == 0:
            optimo [i] = optimo[i//2] + 1
        else:
            optimo [i] = optimo[i-1] + 1
    print(optimo)
    return optimo[k]


k = 6609555
print(len(operaciones(k)))
print(ejercicio11(k))