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
            saidacalculada = calcular_saida(np.asarray(entradas[i]))
            print(f"Entradas -> {entradas[i]} saidas Obtida -> {saidacalculada} SaidaEsperada -> {saidas[i]}")
            erro= saidas[i] - saidacalculada
            erroTotal += erro
            print(erroTotal)
            for x in range(len(pesos)):
                pesos[x] = pesos[x] + (taxaAprendizagem * entradas[i][x] * erro)
                print(f"Peso atualizado: {pesos[x]} ")
            
            
            if erroTotal == 0:
                print("\033[32mpesos ajustados com sucesso:\033[m")
            print(f"Total de erros:{erroTotal}")
        novos_pesos = pesos


treinar()