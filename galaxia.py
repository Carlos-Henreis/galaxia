import math
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
#Definindo as constantes (em UA e Ms)
G = 6.67e-11
M = 10e12

#Leitura do passoaa
N = int(input("Digite o numero de estrelas da galaxia: "))
n = int(input("Digite o numero de itaracoes para a evolucao da galaxia: "))
#Condições iniciais
estrelas = np.random.normal(0,1,[N, 2])#Matriz para armazenar a posição das estrelas, e gera as posições iniciais das estrelas
estrelas = estrelas*10e10#Multiplico cada elemento da matriz por 10¹⁰

vEstrelas = []
vx = []
vy = []

for estrela in estrelas:#Para cada linha da matriz....
    velocidade = sqrt((G*M)/(sqrt(estrela[0]**2+estrela[1]**2)))#Calcula a velocidade
    componenteVX = -((velocidade * estrela[0]) / (sqrt(estrela[0]**2+estrela[1]**2)))
    componenteVY = (velocidade * estrela[1]) / (sqrt(estrela[0]**2+estrela[1]**2))
    vEstrelas.append(velocidade)  # Adiciona no vetor de velocidades
    #Adiciona as componentes das velocidades
    vx.append(componenteVX)
    vy.append(componenteVY)

vEstrelas = np.array(vEstrelas)#Converte o vetor para um vetor numpy
vx = np.array(vx)
vy = np.array(vy)
#Fim das condições iniciais

#"Iniciando" o gráfico
plt.title('Galaxia')
plt.xlabel('Posicao (UA) ')
plt.ylabel('Posicao(UA)')
scat = plt.scatter([x[0] for x in estrelas], [y[1] for y in estrelas], color='black', s=2)
plt.pause(0.006)
scat.remove()

for i in range(n):
    for idx, estrela in enumerate(estrelas):
        deltaT = 10e9/2 if i == 0 else 10e9
        vx[idx] = vx[idx] + (deltaT * (estrela[0] / sqrt(estrela[0] ** 2 + estrela[1] ** 2)) * sqrt((G * M) / (sqrt(estrela[0] ** 2 + estrela[1] ** 2))))
        vy[idx] = vy[idx] + (deltaT * (estrela[1] / sqrt(estrela[0] ** 2 + estrela[1] ** 2)) * sqrt((G * M) / (sqrt(estrela[0] ** 2 + estrela[1] ** 2))))
        deltaT = 10e9
        estrela[0] = estrela[0] + (vx[idx]*deltaT)
        estrela[1] = estrela[1] + (vy[idx] * deltaT)
    scat = plt.scatter([x[0] for x in estrelas], [y[1] for y in estrelas], color='black', s=2)
    plt.pause(0.006)
    scat.remove()

scat = plt.scatter([x[0] for x in estrelas], [y[1] for y in estrelas], color='black', s=2)
plt.pause(0.006)
plt.show()
