# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:35:44 2017

@author: lucas
"""

from numpy import linspace
import matplotlib.pyplot as plt

length = 0.5 #tamanho lado quadrado (em m)
dist_step = 0.125 #distancia entre os pontos no quadrado (em m)
time_step = float(0.001) #de quanto em quanto temp roda a simulação (em s)
time_limit = 200 #qual a duracao da simulacao (em s)
term_difus = 1 #coef. de difusividade termica

center_temp  = 0 #temperatura na placa (sem contar as bordas) em graus
time = linspace(0,time_limit,(time_limit/time_step)+1) #lista com os tempos de simulacao
dist = linspace(0,length,(length/dist_step)+1) #lista com as distancias lineares dos pontos

old_tempo = [[0 for x in range(0,int(length/dist_step+1))] for y in range(0,int(length/dist_step+1))] #matriz de temperatura da placa no tempo antigo (um anterior ao tempo atual)
new_tempo = old_tempo #matriz de temperatura do tempo atual (começa com o tempo antigo e vai se atualizando conforme o tempo passa)

lambda_const = ((term_difus*time_step)/(dist_step*dist_step)) #equivalente ao F0 da equacao da folhinha

#flags que indicam se cada borda esta isolada ou nao
fixed_border_r = False
fixed_border_l = False
fixed_border_u = False
fixed_border_d = True


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

#neste for triplo, j representa a coluna da mattriz de temperatura, i a linha, e k o tempo (por quanto tempo vai rodar)
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
    
    

