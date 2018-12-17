# -*- coding: utf-8 -*-
"""
This code is created by Achari to solve the Monty hall problem psed by Professor Tip-Wah Chung,.
narayanachari.kvlv@gmail.com
"""

#%% Import nrcessary packages
import numpy as np

#%% 
n=10000
print("==================================================================")
print("Here you go !!!")
print("I am going to run the Monty Hall selection problem ",n, " times,")
print("and check to see is it any better to changet the initial selection.")
print( )
 # number of trials
hits_without_change=0
for i in range(n):
    doors=np.zeros(3)
    index=np.random.randint(0,3)
    doors[index]=1 # randomly places a gift in one of the three doors
    choice=np.random.randint(0,3) #select one of the doors randomly
    if doors[choice]!=0:
        hits_without_change+=1
hits_with_change=n-hits_without_change #Assuming Monty always opens one of the doors with zeros ie. no gift
print("Probability to get the gift")
print("          Without change of selection = ", hits_without_change/n)
print("          With change of selection    = ", hits_with_change/n)
print( )
print('After running the trial for ', n,' times, it seems, it is better to reconsider the selection!')
print("==================================================================")
