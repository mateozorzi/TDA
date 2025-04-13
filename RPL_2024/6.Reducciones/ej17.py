"""
En el reino de Gondor ha incrementado enormemente la delincuencia luego de su urbanización. 
El rey Aragorn no quiere que todo su esfuerzo en construir calles resulte en vano, 
por lo que quiere poner guardianes a vigilar las calles por las noches. 
El problema es que cuesta mucho dinero entrenar a dichos guardianes, 
por lo que quiere reducir al mínimo la cantidad que sean necesarios entrenar. 
Sabe que cada guardian puede estar vigilando desde una esquina, 
y desde allí tener visibilidad hasta cualquier otra esquina directa. 
Necesita determinar la cantidad mínima de guardianes que son necesarios para cubrir todas las calles de su reino. 
Como primera medida, consulta con el oráculo Alumnus Teorius Algoritmus (es decir, quien lee esta consigna), 
para determinar si esto es conseguible en corto tiempo (el oráculo le pregunó algo sobre tiempo polinomial, 
que Aragorn no entendió y le dijo “si, eso”). Tenemos que explicarle a Aragorn que este pedido no es realizable 
(y debe armarse de paciencia, o no buscar el mínimo exacto), 
porque el problema de Guardianes de Gondor es, en realidad, un problema NP-Completo 
(en su versión de problema de decisión: “¿Se pueden vigilar todas las calles con esta topología con un máximo de K guardianes?”).
"""

"""
Problema de desicion:
Gondor: ¿Se pueden vigilar todas las calles con esta topología con un máximo de K guardianes?

Se trata de la busqueda de DM minimo, al ser un problema NP-C, no se conoce una solucion entimepo polinomial

Porque es NP-C
Yo conozoco VC es NP-C
entonces reduzco:
VC <=p DM
creo un nuevo grafo
Por cada arista del grafo original, agrego un vertice que este unido a los dos vertices que se unene en la arista
si hay un DS de tamaño k en el nuevo grafo, hay un VC de tamaño k en el grafo original



con HS???????
"""