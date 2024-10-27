import numpy as np
entradas = np.array([1,7,5])
entradas2 = np.array([-1,7,5])
pesos = np.array([0.8,0.1,0])
# melhorando o processo do somatorio
def somatorio(e,p):
    #dot product / produto escalar
    #metodo do np.array 
    produto_escalar = e.dot(p)
    return produto_escalar


print(somatorio(entradas,pesos))

def stepfunction(somatorio):
    if somatorio > 0:
        return 1
    return 0

r = stepfunction(somatorio(entradas,pesos))
r2 = stepfunction(somatorio(entradas2,pesos))

print(r)
print(r2)
