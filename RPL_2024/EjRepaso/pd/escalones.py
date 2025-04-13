#Ec de recurrencia:
# opt[i] = opt[i-1] + opt[i-2] + opt[i-3]
def escalones(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    pasosEscalonAnterior = 2
    pasosEscalonAnteriorA = 1
    pasosEscalonAnteriorAA = 1
    
    for i in range(3,n+1):
        cantPasos = pasosEscalonAnterior + pasosEscalonAnteriorA + pasosEscalonAnteriorAA
        pasosEscalonAnteriorAA = pasosEscalonAnteriorA
        pasosEscalonAnteriorA = pasosEscalonAnterior
        pasosEscalonAnterior = cantPasos

    return cantPasos

print(escalones(5)) #13