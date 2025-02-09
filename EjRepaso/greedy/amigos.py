import grafo

def conexiones(conocidos):
    g = grafo.Grafo()
    
    agregados = set()
    for p1,p2 in conocidos:
        if p1 not in agregados:
            g.agregar_vertice(p1)
        if p2 not in agregados:
            g.agregar_vertice(p2)
        
        g.agregar_arista(p1,p2,1)
    
    return g

#conocidos, tupla de socios que se conocen
def fiesta(conocidos):
    invitados = []

    g = conexiones(conocidos)

    socios = g.obtener_vertices()

    desInvitado = True
    while desInvitado:
        desInvitado = False
        for s in socios:
            if len(g.adyacentes(s)) < 4:
                g.borrar_vertice(s)
                desInvitado = True
        socios = g.obtener_vertices()
    
    invitados = g.obtener_vertices()

    return invitados
"""
Regla greedy: Por cada iteracion de socios, veo cuantos conocidos tiene x persona. Si tiene menos de cuatro
lo elimino y actualizo la lista de socios para ver si algun otro se quedo con menos de 4 conocidos. Si se
realiza una pasada completa sin elimiar invitados, significa que los que qeudan conocen a por lo menos cuatro
personas cada uno, Estan habilitados para ir a la fiesta
Sera el resultado optimo, porque cada vez que se elimina una persona de la lista, se corroborara por lo menos una vez mas
si con esta actualizacion queda alguna persona con menos de 4 conocidos. Si Maria conocia a Jose, Mateo, Martin y Renata
y Renata solo conocia a 1 persona, primero se elimina Renata y como es eliminada ahora Maria solo conoce 3 personas,
por lo que tampoco sera invitada
"""


more_names_pairs = [
    ("Alice", "Bob"),
    ("Charlie", "David"),
    ("Eve", "Frank"),
    ("Grace", "Henry"),
    ("Isabel", "John"),
    ("Kevin", "Linda"),
    ("Mary", "Nathan"),
    ("Olivia", "Peter"),
    ("Quinn", "Rachel"),
    ("Sarah", "Thomas"),
    ("Henry", "Isabel"),
    ("Nathan", "Olivia"),
    ("Peter", "Quinn"),
    ("Rachel", "Sarah"),
    ("Thomas", "Alice"),
    ("Bob", "Charlie"),
    ("David", "Eve"),
    ("Frank", "Grace"),
    ("Henry", "Isabel"),
    ("John", "Kevin"),
    ("Alice", "Bob"),
    ("Charlie", "David"),
    ("Eve", "Frank"),
    ("Grace", "Henry"),
    ("Isabel", "John"),
    ("Grace", "John"),
    ("Grace", "Isabel"),
    ("Grace", "Peter"),
    ("Isabel", "Peter"),
    ("Rachel", "Peter"),
    ("Rachel", "Thomas"),
    ("Mateo", "1"),
    ("Mateo", "2"),
    ("Mateo", "3"),
    ("Mateo", "4"),
    ("1", "2"),
    ("1", "3"),
    ("1", "4"),
    ("2", "3"),
    ("2", "4"),
    ("3", "4"),
]

print(fiesta(more_names_pairs))