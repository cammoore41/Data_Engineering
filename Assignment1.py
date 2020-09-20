# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Import packages
import numpy as np
import pandas as pd
from timeit import default_timer as timer
import matplotlib.pyplot as plt

#Set random seed
np.random.seed(30)

#Generate random data
a=np.random.randint(0, 10000, 512)
b=np.random.randint(0, 10000, 1024)
c=np.random.randint(0, 10000, 2048)
d=np.random.randint(0, 10000, 4096)
e=np.random.randint(0, 10000, 8192)

#Length of Arrays
Length=[]
for i in [a,b,c,d,e]:
    Length.append(len(i))

#sort data
Sort=[]
for i in [a,b,c,d,e]:
    start=timer()
    i.sort()
    end=timer()
    elapsed_time=(end-start)*100
    Sort.append(elapsed_time)

#Binary Search Algorithm
def binarySearch(list, item):
        low = 0
        high = len(list) - 1
        while (low <= high):
            mid=((low+high)//2)
            if list[mid]==item:
                return(mid)
            else:
                if list[mid]>item:
                    high=mid-1
                else:
                    low=mid+1
        return
    
#Linear Search Algorithm
def linearsearch(list, item): 
    for i in range (0, len(list)): 
        if (list[i] == item): 
            return i; 
    return

#Time for each search
#Binary
Binary=[]
for i in [a,b,c,d,e]:
    start=timer()
    binarySearch(i, max(i))
    end=timer()
    elapsed_time=(end-start)*100
    Binary.append(elapsed_time)

#Linear
Linear=[]
for i in [a,b,c,d,e]:
    start=timer()
    linearsearch(i, max(i))
    end=timer()
    elapsed_time=(end-start)*100
    Linear.append(elapsed_time)

#Create dataframe
rows=[]
df=pd.DataFrame(rows, columns=['Length',
                               'Sort Time (ms)',
                               'Linear (ms)',
                               'Binary (ms)',
                               'Binary + Sort (ms)'])

#Add data to dataframe
df['Length']=Length
df['Sort Time (ms)']=Sort
df['Linear (ms)']=Linear
df['Binary (ms)']=Binary
df['Binary + Sort (ms)']=np.add(Binary,Sort)

#Create first plot
plt.plot(df['Length'],df['Linear (ms)'], label='Linear')
plt.plot(df['Length'],df['Binary (ms)'], label='Binary')
plt.xlabel('Size of Array')
plt.ylabel('Execution Time (ms)')
plt.legend()
plt.show()

#Create second plot
plt.plot(df['Length'],df['Sort Time (ms)'], label='Sort')
plt.plot(df['Length'],df['Linear (ms)'], label='Linear')
plt.plot(df['Length'],df['Binary (ms)'], label='Binary')
plt.plot(df['Length'],df['Binary + Sort (ms)'], label='Binary+Sort')
plt.xlabel('Size of Array')
plt.ylabel('Execution Time (ms)')
plt.legend()
plt.show()