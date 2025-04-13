def posicion_pico(v, ini, fin):
    if(ini == fin):
        return ini
    
    mitad = (ini + fin) // 2
    if(v[mitad] > v[mitad + 1] and v[mitad] > v[mitad - 1]):
        puntoP = mitad
    elif(v[mitad] > v[mitad + 1]):
        puntoP = posicion_pico(v, ini,mitad-1)
    else:
        puntoP = posicion_pico(v, mitad+1,fin)
    
    return puntoP


arr = [1,2,3,2,1,0,-1]
pos = posicion_pico(arr,0,len(arr)-1)
print(pos)