import numpy as np
import random
import matplotlib.pylab as plt

lis=(0,1,2,3,4,5,6,7,8)
print 'lis=',lis

#==============================================================================
# Add all the lelemnts of a list
#==============================================================================
summ=reduce(lambda a, x:x+a, lis)
print 'summ=',summ

#==============================================================================
# Square of each element in a list
#==============================================================================
sqr=map(lambda x:x*x, lis)
print 'sqr=',sqr

#==============================================================================
# Add random number to elements in a list
#==============================================================================
lis_random=map(lambda x:x+random.uniform(-1,1),lis)
lis_random=np.round( [float(i) for i in lis_random], 2)
print 'lis_random=',lis_random




