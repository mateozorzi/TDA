"""
lo mimso que el ej9 pero en O(n)
"""

def mas_de_la_mitad_dyc(arr):
    if len(arr) == 1:
        return arr[0]
    
    mitad = len(arr) // 2

    izq = arr[:mitad]
    der = arr[mitad:]

    candidatos = mas_de_la_mitad_dyc(izq)

    


def mas_de_la_mitad(arr):
    return False

#Complejidad -> T(n) = AT(n/B) + O(n^c) -> T(n) = T(n/2) + O(n) -> A = 1, B = 2, C = 1, por TM logB(A) < C -> O(n)
#genero uin nuevo arreglo, con menos elementos (n/2 elementos), si un elemento esta mas de la mitad de las veces, matematicamente
#esta obligado a estar uno al lado de otro por lo menos una vez
#Vemos los elementos de a apres en el arreglo original y veo si esta esta situacion. Cada vez que un veo que un par se repite, lo inseto en este arreglo
#Para el nuevo arreglo que genere, si en el orignal el elemento esta mas de la mitad de las veces, para el nuevo arreglo tambien lo estara
#En otro  caso de que la cantidad sea impar, y no encuentro paquetes de pares repetidos, cuento la cantidad de veces que se repite el ultimo elemento
#que no queda emparejado
#el algortimo deuvelve un candidato, luego cuento si esta mas del amitad de las veces en el orignal O(n)
arr = [1,2,2,1,1,1]