# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:35:44 2017

@author: lucas
"""

from numpy import linspace
import matplotlib.pyplot as plt

length = 50
dist_step = 5
time_step = float(5)
time_limit = 50
term_difus = 1
edges_temp = 50
center_temp  = 80
time = linspace(0,time_limit,(time_limit/time_step)+1)
dist = linspace(0,length,(length/dist_step)+1)

old_tempo = [[0 for x in range(0,length/dist_step+1)] for y in range(0,length/dist_step+1)]
new_tempo = old_tempo

lambda_const = ((term_difus*time_step)/(dist_step*dist_step))


for i in range(0,length/dist_step+1):
    for j in range(0,length/dist_step+1):
        old_tempo[i][j] = center_temp
        if i == 0:
             old_tempo[i][j] = edges_temp
        if i == length/dist_step:
            old_tempo[i][j] = edges_temp
        if j == 0:
            old_tempo[i][j] = edges_temp
        if j == length/dist_step:
            old_tempo[i][j] = edges_temp


for k in range(0,len(time)):
    for i in range(1,len(dist)-1):
        for j in range(1,len(dist)-1):
            new_tempo[i][j] = lambda_const*(old_tempo[i+1][j] + old_tempo[i-1][j] + old_tempo[i][j+1] + old_tempo[i][j-1]) + (1 - 4*lambda_const)*old_tempo[i][j]
            print(new_tempo[i][j])
    

    old_tempo = new_tempo
    plt.imshow(new_tempo, cmap='hot', interpolation='nearest')
    plt.show()
    
    

