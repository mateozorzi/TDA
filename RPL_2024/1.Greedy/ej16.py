"""El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios. 
Sin embargo por protocolo cada persona invitada debe cumplir un requisito: 
Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas. Dada un lista de tuplas (duplas) de personas que se conocen:
a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema."""

# conocidos: lista de pares de invitados que se conocen, cada elemento es un (a,b)
import grafo
def obtener_invitados(conocidos):
    g = grafo.Grafo()
    for par in conocidos:
        if par[0] not in g:
            g.agregar_vertice(par[0])
        if par[1] not in g:
            g.agregar_vertice(par[1])
        if not g.estan_unidos(par[0],par[1]):
            g.agregar_arista(par[0],par[1],1)

    huboDesinvitados = True
    while huboDesinvitados:    
        huboDesinvitados = False
        for persona in g.obtener_vertices():
            if len(g.adyacentes(persona)) < 4:
                g.borrar_vertice(persona)
                huboDesinvitados = True
    return g.obtener_vertices()


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

print(obtener_invitados(more_names_pairs))