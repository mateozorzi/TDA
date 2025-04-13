class Automata:
    def __init__(self):
        self.estados = {}
        self.estado_inicial = None
        self.estados_finales = set()
        self.transiciones = {}

    def estado(self, nombre, es_inicial=False, es_final=False):
        if nombre in self.estados:
            raise ValueError(f"El estado '{nombre}' ya existe.")
        
        self.estados[nombre] = {}
        
        if es_inicial:
            if self.estado_inicial is not None:
                raise ValueError("Ya existe un estado inicial.")
            self.estado_inicial = nombre
        
        if es_final:
            self.estados_finales.add(nombre)

    def transicion_estado(self, nombre1, nombre2, simbolo):
        if nombre1 not in self.estados or nombre2 not in self.estados:
            raise ValueError("Uno o ambos estados no existen.")
        
        if simbolo not in self.transiciones:
            self.transiciones[simbolo] = {}
        
        if nombre1 not in self.transiciones[simbolo]:
            self.transiciones[simbolo][nombre1] = []
        
        self.transiciones[simbolo][nombre1].append(nombre2)

# Ejemplo de uso:
# automata = Automata()
# automata.estado("q0", es_inicial=True)
# automata.estado("q1", es_final=True)
# automata.transicion_estado("q0", "q1", "a")