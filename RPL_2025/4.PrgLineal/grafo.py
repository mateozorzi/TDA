class Grafo:
    def __init__(self, dirigido=False, vertices_init=[]):
        self.dirigido = dirigido
        self.vertices = {}  # Diccionario para almacenar los vértices y sus adyacencias
        for v in vertices_init:
            self.agregar_vertice(v)

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}  # Diccionario vacío para almacenar las adyacencias de v

    def borrar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
            # Eliminar todas las adyacencias que involucren a v
            for vertice in self.vertices:
                if v in self.vertices[vertice]:
                    del self.vertices[vertice][v]

    def agregar_arista(self, v, w, peso=1):
        self.agregar_vertice(v)
        self.agregar_vertice(w)
        self.vertices[v][w] = peso
        if not self.dirigido:
            self.vertices[w][v] = peso

    def borrar_arista(self, v, w):
        if v in self.vertices and w in self.vertices[v]:
            del self.vertices[v][w]
            if not self.dirigido and w in self.vertices and v in self.vertices[w]:
                del self.vertices[w][v]

    def estan_unidos(self, v, w):
        return w in self.vertices[v] if v in self.vertices else False

    def peso_arista(self, v, w):
        return self.vertices[v][w] if v in self.vertices and w in self.vertices[v] else None

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def vertice_aleatorio(self):
        import random
        return random.choice(list(self.vertices.keys()))

    def adyacentes(self, v):
        return list(self.vertices[v].keys()) if v in self.vertices else []

    def __str__(self):
        result = ""
        for v in self.vertices:
            for w in self.vertices[v]:
                result += f"{v} {'-->' if self.dirigido else '<-->'} {w} (peso: {self.vertices[v][w]})\n"
        return result.strip()