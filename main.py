# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:35:44 2017

@author: lucas
"""

from numpy import linspace
import matplotlib.pyplot as plt

length = 50
dist_pace = 5
time_pace = float(5)
time_limit = 100
term_difus = 1
edges_temp = 50
center_temp  = 80
time = linspace(0,time_limit,(time_limit/time_pace)+1)
dist = linspace(0,length,(length/dist_pace)+1)

old_temp = [0]*((length/dist_pace)+1)
new_temp = old_temp

lambda_const = ((term_difus*time_pace)/(dist_pace*dist_pace))


for i in range(0,length/dist_pace+1):
    if i == 0:
        old_temp[i] = edges_temp
    elif i == length/dist_pace:
        old_temp[i] = edges_temp
    else:
        old_temp[i] = center_temp

print(old_temp)


for i in range(0,len(time)):
    for j in range(1,len(dist)-1):
        new_temp[j] = old_temp[j] + lambda_const*(old_temp[j+1] - 2*old_temp[j] + old_temp[j-1])
    old_temp = new_temp
    plt.plot(dist, new_temp)
    
    


        

  
    



