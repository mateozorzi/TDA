"""Solucion Top-Down"""
def fib_memorioso (n) :
    M_FIB = [None] * (n+1)
    return fib_rec_memorioso (n, M_FIB)
def fib_rec_memorioso (n, M_FIB) :
    if n == 0:
        return 0
    if n == 1:
        return 1
    if M_FIB [n-1] == None:
        M_FIB [n-1] = fib_rec_memorioso (n-1, M_FIB)
    if M_FIB [n-2] == None:
        M_FIB [n-2] = fib_rec_memorioso (n-2, M_FIB)
    M_FIB [n] = M_FIB [n-1] + M_FIB [n-2]
    return M_FIB[n]

"""Solucion Botom-Up iterando"""
def fib_iterativo (n) :
    M_FIB = [None] * (n+1)
    M_FIB [0] = 0
    M_FIB[1] = 1
    for i in range (2, n+1) :
        M_FIB[1] = M_FIB[1-1] + M_FIB[1-2]
    return M_FIB [n]

"""Solucion me quedo solo con los dos anteriores, ocupo menos memoria. O(n) y cte en memoria"""
def fib_dinamico (n) :
    if n == 0:
        return 0
    if n == 1:
        return 1
    anterior = 0
    actual = 1
    for i in range (1, n) :
        nuevo = actual + anterior
        anterior = actual
        actual = nuevo
    return actual

print(fib_dinamico(5))