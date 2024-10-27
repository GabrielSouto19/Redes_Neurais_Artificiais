entradas = [1,7,5]
entradas2 = [-1,7,5]
pesos = [0.8,0.1,0]

def somatorio(e,p):
    s = 0 
    if len(e) == len(p):
        for i in range(len(e)):
            s += e[i]*p[i] 
    else:
        print("A quantidade de entradas devem ser iguais a quantidades de pesos")#viajeei aqui

    return s 

print(somatorio(entradas,pesos))

def stepfunction(somatorio):
    if somatorio >0:
        return 1
    else:
        return 0

r = stepfunction(somatorio(entradas,pesos))
r2 = stepfunction(somatorio(entradas2,pesos))

print(r)
print(r2)
