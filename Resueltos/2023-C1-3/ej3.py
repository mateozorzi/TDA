#bolsas -> lista de enteros, de la cantidad de bolsas de sangre
#disponibles de S0,SA,SB,SAB
#Personas -> cantidad de pacientes por tipo de sangre

#regla greedy: EN cada iteracion se buscara el grupo de sangre con mas demanda, se le atendera 
# con la sangre que mayor bolsas tenga en stock en el momento y que pueda recibir (optimo local), 
# asi buscando maximizar la cantidad de paciente atendidios
# La complejidad del algoritmo, dado que la cantidad de tipo de sangre en s = 4
# la complejidad esta dada por la cantidad de acientes que peuden ser atendidos.
#si hay n pacientes ecperando entonces la complejidad del algoritmo seria
# O(n * s) = O(n) ya que s = 4
def laboratorio(bolsas, personas):
    cantidadPacientes = sum(personas)
    pacientesAtendidos = 0

    tipoA, tipoB, tipoAB, tipoCero = 0, 1, 2, 3

    while sum(personas) > 0 and sum(bolsas) > 0:
        #busco que tipo de sangre es la mas necesitada
        tipoMax = 0
        demandaMax = 0
        for i in range(len(personas)):
            if personas[i] > demandaMax:
                demandaMax = personas[i]
                tipoMax = i
        
        #Atiendo a un paciente de tipo de sangre mas necesitado
        if tipoMax == tipoCero :
            if bolsas[tipoCero] > 0:
                #si hay bolsas
                personas[tipoCero] -= 1
                bolsas[tipoCero] -= 1
                pacientesAtendidos += 1
            else:
                #si no hay mas bolsas, no puedo atender mas pacientes
                personas[tipoCero] = 0
        elif tipoMax == tipoA:
            if bolsas[tipoA] > 0 or bolsas[tipoCero] > 0:
                #si hay bolsas
                if bolsas[tipoA] > bolsas[tipoCero]:
                    #hay mas bolsas del tipo A
                    personas[tipoA] -= 1
                    bolsas[tipoA] -= 1
                else:
                    #hay mas bolsas del tipo 0
                    personas[tipoCero] -= 1
                    bolsas[tipoCero] -= 1
                
                pacientesAtendidos += 1
            else:
                #si no hay mas bolsas, no puedo atender mas pacientes
                personas[tipoA] = 0
        elif tipoMax == tipoB:
            if bolsas[tipoB] > 0 or bolsas[tipoCero] > 0:
                #si hay bolsas
                if bolsas[tipoB] > bolsas[tipoCero]:
                    #hay mas bolsas tipo B
                    personas[tipoB] -= 1
                    bolsas[tipoB] -= 1
                else:
                    #hay mas bolsas tipo 0
                    personas[tipoCero] -= 1
                    bolsas[tipoCero] -= 1
                pacientesAtendidos += 1
            else:
                #si no hay mas bolsas, no puedo atender mas pacientes
                personas[tipoB] = 0
        else: #tipo AB
            if sum(bolsas) > 1:
                #si hay bolsas
                maxCantidad = 0
                maxBolsa = 0
                for j in range(len(bolsas)):
                    if bolsas[j] > maxCantidad:
                        maxCantidad = bolsas[j]
                        maxBolsa = j
                bolsas[maxBolsa] -= 1
                personas[tipoAB] -= 1
                pacientesAtendidos += 1
            else:
                #si no hay mas bolsas, no puedo atender mas pacientes
                personas[tipoAB] = 0
        
    if pacientesAtendidos == cantidadPacientes:
        return True
    
    return False

            

bolsas = [30,12,10,20] #sum(bolsas) = 72
personas = [43,10,3,42] #sum(personas) = 98
print(laboratorio(bolsas, personas)) #deberia devolver True