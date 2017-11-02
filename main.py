# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:35:44 2017

@author: lucas
"""

from numpy import linspace
import matplotlib.pyplot as plt
#test commmit

length = 50
dist_step = 5
time_step = float(5)
time_limit = 100
term_difus = 1
edges_temp = 50
center_temp  = 80
time = linspace(0,time_limit,(time_limit/time_step)+1)
dist = linspace(0,length,(length/dist_step)+1)

old_temp = [0]*((length/dist_step)+1)
new_temp = old_temp

lambda_const = ((term_difus*time_step)/(dist_step*dist_step))


for i in range(0,length/dist_step+1):
    if i == 0:
        old_temp[i] = edges_temp
    elif i == length/dist_step:
        old_temp[i] = edges_temp+10
    else:
        old_temp[i] = center_temp

print(old_temp)


for i in range(0,len(time)):
    for j in range(1,len(dist)-1):
        new_temp[j] = old_temp[j] + lambda_const*(old_temp[j+1] - 2*old_temp[j] + old_temp[j-1])
    old_temp = new_temp
    plt.plot(dist, new_temp)
    
    


        

  
    



