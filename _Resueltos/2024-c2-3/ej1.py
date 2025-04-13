def balanceada(cadena):

    par_izq = 0
    par_der = 0

    largo = 0

    for c in cadena:
        if c == '(':
            par_izq += 1
        elif c == ')':
            par_der += 1
        
        if par_der > par_izq:
            break

        largo += 1

    return largo


cadena = "()()()()(())()(()"
print(balanceada(cadena))  # 6

#Regla gredy: contar la catnidad de parentesis de la cadena hasta terminar o encontrar una cantidad de parentesis derechos mayor a la de izquierdos
#Es optimo, ya que para estar balanceada debe haber la misma cantidad de parentesis de ambos tipos, si hay mas derechos se cerraron mas de la cuenta por l que queda desbalanceda