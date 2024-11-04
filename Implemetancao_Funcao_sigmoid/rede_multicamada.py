# y = 1/1+e^-x 

#Função Sigmoid

import numpy as np 

def sigmoid (somatorio):
    return 1 / (1+ np.exp(-somatorio))
# quanto maior o somatorio mais o retorno se aproxima de 1 
#np.exp numero de euler
a = sigmoid(50)
print(a)

# ativação da camada oculta

# tabela xor
#  0 0  0   
#  0 1  1
#  1 0  1
#  1 1  0
#começamos com um conjunto de pesos aleatorio e logo apos ela vai se ajustando 

#aplicação da nossa função soma para cada neuronio 
#ativação da camada oculta II

entradas = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1],
])
saidas = np.array([0,1,1,0])

pesos0 = np.array([[-0.424,-0.740,-0.961],
                  [0.358,-0.577,-0.469]])


pesos1 = np.array([-0.017,-0.893,-0.148])

epocas = 100 # oque são essas epocas
#quantidades de vezes qwe eu vou passar atualizando os pesos

for i in range(epocas):
    #teste de como ele vai se adaptar nos ajustes de pesos
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada,pesos0)#vai fazer a soma e a multiplicação dos elementos correspondentes
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta,pesos1)
    camadasSaidas = sigmoid(somaSinapse1)
