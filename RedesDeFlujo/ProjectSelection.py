"""
Ejemplo: Project Selection
Tenemos proyectos que podemos realizar. Algunos dan ganancia positiva y otros
negativa. Hay dependencias: puede que para hacer un proyecto i también
tengamos que hacer un proyecto j, sin ciclos.

un proyecto negativo sin proyceto positivo que dependa de este, no lo hago
Un proyeecto de ganancia positiva que no depende de negativo, lo hago
Conviene resolver por corte minimo
de la fuente a los proyectos, la ganancia que dan
de los proyectos al sumidero las perdidas
a las aristas que conectan proyectos le ponemos infinito, no me interesa este peso
Si hago el corte minimo, veo como se compensan los pesos y si me conviene hacer tal proyecto
si el corte esta con la fuente aumenta la ganancias, sino auientan las perdidas
"""