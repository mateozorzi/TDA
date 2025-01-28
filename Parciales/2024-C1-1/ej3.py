"""
El problema del cumpleaños de Coty puede enunciarse como: Dada la lista de n invitados al cumpleaños de Coty, un
número k, y conociendo quién se conocen con quién (ej: una lista con los pares de conocidos), ¿existe una forma de
asignar a lo sumo k personas para dar los regalos, de tal forma que todos los invitados, al hablar luego con quienes se
conozcan, puedan hablar del regalo que obtuvo uno o bien el otro?
PC es NP-C?

Probl de decision:
Puedo conseguir a lo sumo k personas, dado que luego pueden hablar entre ellas del regalo que recibio uno de los dos?

Veo si es NP, creando un validador polinomial

Para probar PC es NP-C, debo reducir un problema ya conocido como NP-C
En este caso reduzco:
Vertex Cover <=p PC

Dado el grafo, creo un par de vertics conocidos si tienen una arista en comun. Si u y v estan unidos, habra un par (u,v)
Luego quiero encontrar k vertices dado que por cada arista haya al menos uno de estos en la solucion. Por lo que al usar la caja negra que resuelve
el problema del cumpleaños le pasare los pares de vertices unidos, y el k sera el mismo.

Si hay VC, habra un PC valido?
Si k vertices, cumplen que para toda arista, en el conjunto solucion esta este o al que se une, habra un VC. Estos k vertices en el problema del cumpleaños serian las k personas qeu buscamos,
y dadas su conexiones (par de conexion con otra persona), todas los invitados del cumpleaños podrian hablar con otro del reaglo recibido por alguno de los dos. Por lo que para ninguna conexion de dos invitados
ninguno de los dos tendra regalo, ya que seria absurdo si existe un VC.

si y solo si

Si hay un PC, habra un VC valido?
Si encuentro k invitados, dado que sus conexiones. Todos los invitados pueden habalr con un conocdio acerca del regalo que recibieron o del que ricibio el otro, dado que en mi reduccion
los pares de conocidos simbolizan las conexiones de vertices en el grafo, cada invitado es un vertice del grafo, entonces habra k vertices, dado que para cada arista, uno de los dos estara en la solucion (uno de los dos podra hablar de su regalo)


"""

def validador(conexiones, k , solucion):
    if len(solucion) < k: #me fijo que alo sumo sean k personas
        return False
    
    for p1,p2 in conexiones: #para cada conexion, al menos una de las dos personas debe estar en la solucion
        if p1 not in solucion and p2 not in solucion:
            return False
    
    return True