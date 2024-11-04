import numpy as np
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1


def stepfunction(somatorio):
    if somatorio > 0:
        return 1
    return 0

def calcular_saida(registro):
    somatorio = registro.dot(pesos)
    return stepfunction(somatorio)

def treinar():
    erroTotal = 1
    while erroTotal != 1:
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calcular_saida(np.asarray(entradas[i]))
            if saidaCalculada != saidas[i]:
                erroTotal +=1
        for i in range(pesos):
            pass 


    print(erroTotal)




treinar()