"""
Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que no pueden llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

En el ejemplo de código inicial de la actividad mostramos un llamado de ejemplo a la función balanza, a la que se le deben pasar los dos conjuntos de joyas a verificar. La cantidad de joyas en cada conjunto debe ser la misma, para que el resultado de la balanza de platillos nos dé información.
Si los dos platillos pesan lo mismo, balanza devuelve 0.
Si el primer platillo es más pesado, balanza devuelve 1.
Si el segundo platillo es más pesado, balanza devuelve -1.
"""
def balanza(arr1, arr2):
    aux1 = sum(arr1)
    aux2 = sum(arr2)

    if aux1 > aux2:
        return 1
    elif aux2 > aux1:
        return -1
    else:
        return 0

def encontrar_joya(joyas):
    return encontrar_joya_dyc(joyas,0,len(joyas))


def encontrar_joya_dyc(joyas,inicio, fin):
    if fin - inicio == 1:
        return inicio
    
    mitad = (inicio+fin) // 2

    izq = joyas[inicio:mitad]
    der = joyas[mitad:fin]

    if len(der) > len(izq):
        fin -= 1
        der.pop()

    res = balanza(izq, der)
    if res == 1:
        return encontrar_joya_dyc(joyas, inicio, mitad)
    elif res == -1:
        return encontrar_joya_dyc(joyas, mitad, fin)
    else:
        return fin


j = [1, 0]
print(encontrar_joya(j))

"""
[1, 0]

[0, 1]

[1, 0, 0]

[0, 1, 0]

[0, 0, 1]

[0, 0, 1, 0]

[0, 0, 1, 0, 0]

[0, 0, 0, 0, 0, 1]

[0, 0, 0, 0, 0, 0, 1]
"""