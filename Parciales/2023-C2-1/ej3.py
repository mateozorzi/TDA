def calculoOptimos(k):
    optimos = [0] * (k+1)

    for i in range(1,len(optimos)):
        if i % 2 == 0:
            optimos[i] = min(optimos[i-1], optimos[i//2]) + 1
        else:
            optimos[i] = optimos[i-1] + 1

def cantOp(k):
    optimos = calculoOptimos(k)