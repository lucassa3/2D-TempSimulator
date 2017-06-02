# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:35:44 2017

@author: lucas
"""

from numpy import linspace
import matplotlib.pyplot as plt

file = open("in.txt","r")
entrada = []
with open ("in.txt", "r") as myfile:
    for line in myfile:
        entrada.append(line)

for i in range(0, 26):
    #print(str(i) +" "+ entrada[i])
    if i == 16:
        length = float(entrada[i]) #tamanho lado quadrado (em m)
    elif i == 17:
        dist_step = float(entrada[i]) #distancia entre os pontos no quadrado (em m)
    elif i == 18:
        time_limit = float(entrada[i]) #qual a duracao da simulacao (em s)
    elif i == 19: 
        time_step = float(entrada[i]) #de quanto em quanto temp roda a simulação (em s)
    elif i == 20:
        term_difus = float(entrada[i]) #coef. de difusividade termica
    elif i == 21:
        center_temp = float(entrada[i]) #temperatura na placa (sem contar as bordas) em graus

    #flags que indicam se cada borda esta isolada ou nao        
    elif i == 22:
        if(entrada[i] == "True\n"):
            fixed_border_r = True
        else:
            fixed_border_r = False
    elif i == 23:
        if(entrada[i] == "True\n"):
            fixed_border_l = True
        else:
            fixed_border_l = False
    elif i == 24:
        if(entrada[i] == "True\n"):
            fixed_border_u = True
        else:
            fixed_border_u = False
    elif i == 25:
        if(entrada[i] == "True"):
            fixed_border_d = True
        else:
            fixed_border_d = False

time = linspace(0,time_limit,(time_limit/time_step)+1) #lista com os tempos de simulacao
dist = linspace(0,length,(length/dist_step)+1) #lista com as distancias lineares dos pontos

old_tempo = [[0 for x in range(0,int(length/dist_step+1))] for y in range(0,int(length/dist_step+1))] #matriz de temperatura da placa no tempo antigo (um anterior ao tempo atual)
new_tempo = old_tempo #matriz de temperatura do tempo atual (começa com o tempo antigo e vai se atualizando conforme o tempo passa)

lambda_const = ((term_difus*time_step)/(dist_step*dist_step)) #equivalente ao F0 da equacao da folhinha

#preenche o old_tempo com os valores iniciaisde temperatura da placa
for i in range(0,int(length/dist_step+1)):
    for j in range(0,int(length/dist_step+1)):
        old_tempo[i][j] = center_temp
        if i == 0:
             old_tempo[i][j] = 100 #borda superior vale 100 graus
        if i == length/dist_step:
            old_tempo[i][j] = 0 #borda inferior vale 0
        if j == 0:
            old_tempo[i][j] = 75 #borda esq vale 75
        if j == length/dist_step:
            old_tempo[i][j] = 50 #borda dir vale 50

count = 1

#neste for triplo, j representa a coluna da matriz de temperatura, i a linha, e k o tempo (por quanto tempo vai rodar)
for k in range(0,len(time)):
    for i in range(0,len(dist)):
        for j in range(0,len(dist)):
            #equacao usada se a borda superior tiver isolada
            if fixed_border_u == True and i == 0 and j>0 and j<len(dist)-1:
                new_tempo[i][j] = lambda_const*(2*old_tempo[i+1][j] + old_tempo[i][j+1] + old_tempo[i][j-1]) + (1 - 4*lambda_const)*old_tempo[i][j]

            #equcao usada se a borda esquerda tiver isolada
            if fixed_border_l == True and j == 0 and i > 0 and i<len(dist)-1:
                new_tempo[i][j] = lambda_const*(old_tempo[i+1][j] + old_tempo[i-1][j] + 2*old_tempo[i][j+1]) + (1 - 4*lambda_const)*old_tempo[i][j]

            #direita
            if fixed_border_r == True and j == len(dist)-1 and i > 0 and i<len(dist)-1:
                new_tempo[i][j] = lambda_const*(old_tempo[i+1][j] + 2*old_tempo[i-1][j] + old_tempo[i][j-1]) + (1 - 4*lambda_const)*old_tempo[i][j]

            #inferior
            if fixed_border_d == True and i == len(dist)-1 and j > 0 and j<len(dist)-1:
                new_tempo[i][j] = lambda_const*(2*old_tempo[i-1][j] + old_tempo[i][j+1] + old_tempo[i][j-1]) + (1 - 4*lambda_const)*old_tempo[i][j]

            #se nao for borda, faz a equcao normal
            if i>0 and j>0 and i<len(dist)-1 and j<len(dist)-1:
                new_tempo[i][j] = lambda_const*(old_tempo[i+1][j] + old_tempo[i-1][j] + old_tempo[i][j+1] + old_tempo[i][j-1]) + (1 - 4*lambda_const)*old_tempo[i][j]
    

    old_tempo = new_tempo

plt.imshow(new_tempo, cmap='bwr', interpolation='nearest')
plt.show()
    
    
    