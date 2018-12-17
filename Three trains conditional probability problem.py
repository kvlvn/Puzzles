# -*- coding: utf-8 -*-
"""
This code is created by Achari to solve the three train problem posed by Professor Yip-Wah Chung. 
narayanachari.kvlv@gmail.com
"""

#%% Import nrcessary packages
import numpy as np
#%% Three trains conditional probability problem.
# Train A arrives at every 10 min (600 sec)
# Train B arrives at every 20 min (1200 sec)
# Train C arrives at every 30 min (1800 sec)
# If the train schedule is unknown what is the probability of to get on to each one of the trains?

def Schehule():
    times=np.array((np.random.randint(0,600),np.random.randint(0,1200),np.random.randint(0,1800)))
    return times

#%%
repeat=list()
for i in range(1000000):
    repeat.append(Schehule().argmin(axis=0))
print('Repeated the random events a million times')
print('Here are the numerical probability to get on to each train.')
unique, counts = np.unique(repeat, return_counts=True)
#print (np.asarray((unique, counts)).T)
print('P(A)= ',100*counts[0]/sum(counts))
print('P(B)= ',100*counts[1]/sum(counts))
print('P(C)= ',100*counts[2]/sum(counts))