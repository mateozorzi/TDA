"""
Dados los problemas de decisiones de Independent Set y Vertex Cover, 
realizar dos reducciones. 
a. Reducir Independent Set a Vertex Cover. 
b. Reducir Vertex Cover a Independent Set.
"""
#IS <= VC
def ISaVC(grafo,k):
    #mi caja negra es la resolucion de VC
    #Yo se que len(IS) + len(VC) = len(grafo),
    #Entonces si yo se como se resuelve VC, se cuantos elementos tendra mi max IS
    #recibo grafo y la cant de vertices
    cantVertices = len(grafo.vertices())
    if vertex_cover(grafo, cantVertices-k): #si existe un VC de (cantVertices-k), entonces existe un IS de al menos tamaño k
        return True
    return False

#VC <= IS
def VCaIS(grafo,k):
    #mi caja negra es la resolucion de IS
    #Yo se que len(IS) + len(VC) = len(grafo),
    #Yo se como se resuelve IS
    #Si exite in IS de por lo menos (cantV - k),
    #entonces existe un VC de tamaño k

    cantVertices = len(grafo.vertices())
    if independent_set(grafo,cantVertices-k):
        return True
    return False