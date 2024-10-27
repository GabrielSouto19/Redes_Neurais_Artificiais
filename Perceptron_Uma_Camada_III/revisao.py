import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0,0,1])
pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1


def stepFunction(somatorio):
    if somatorio >= 1:
        return 1 
    return 0

def calcular_saida(registro):
    somatorio = registro.dot(pesos)
    return stepFunction(somatorio=somatorio)

def treinar():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidas)):
            calculo = calcular_saida(entradas[i])
            print(f"Entradas -> {entradas[i]} saidas Obtida -> {calculo} SaidaEsperada -> {saidas[i]}")
            erroTotal += saidas[i] - calculo
            print(erroTotal)
        novos_pesos = pesos


treinar()