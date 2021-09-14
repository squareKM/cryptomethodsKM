import pandas as pd
import numpy as np
from scipy.stats import bernoulli
#import seaborn as sb
from functools import reduce



prob = pd.read_csv("prob_17.csv")
table = pd.read_csv("table_17.csv")
table_array = np.array(table)#СТ - ОТ, СТР - К
prob_array = np.array(prob)#1 - ОТ, 2 - К

def CM_finder(x,y,z,q):#произведение Р(К)*P(M)
#z - индекс ШТ, q - матрица распределения ШТ
  if table_array[x][y] == z:
    q[z] += prob_array[0][y] * prob_array[1][x]
    
def zeromatrix(n,k):
    listofzeros = [0] * n
    for i in range(n): 
        listofzeros[i] = [0] * k
    return listofzeros

def zerolist(n):
    listofzeros = [0] * n
    return listofzeros

PC = zerolist(20)

#Распределение шифротекста
for i in range(20): 
  for j in range(20):
    for k in range(20):
      CM_finder(i,j,k,PC)

print(np.around(PC,5))
aa = 0
for i in range(0,20,1):
  aa += PC[i]

print("TEST =",np.around(aa,4))

def CM_finder1(x,y,z,q):
  if table_array[x][y] == z:
    q[y][z] += prob_array[0][y] * prob_array[1][x]

PMC = zeromatrix(20,20)

for i in range(20): 
  for j in range(20):
    for k in range(20):
      CM_finder1(i,j,k,PMC)

print(np.around(PMC,4))
aa = 0
for i in range(20): 
  for j in range(20):
    aa += PMC[i][j]

print("TEST =",np.around(aa,4))
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
PM_C = zeromatrix(20,20)

for i in range(20): 
  for j in range(20):
    PM_C[i][j] = PMC[i][j]/PC[j]
print(np.around(PM_C,4))
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
a11 = -1
LOL = zerolist(20)
for i in range(20):
  for j in range(20):
    if PM_C[j][i] > a11:
      a11 = PM_C[j][i]
      LOL[i] = j
  a11 = -1
print(LOL)
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(20):
  print("M[",np.around(LOL[i],4),"] => C[",i,"]")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a22 = 0

for i in range(20):
  a22 += PC[i]*(1-PM_C[LOL[i]][i])# средняя функция потерь 

print(a22)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a33 = 0
a44 = 0

LOL1 = zeromatrix(20,20)

LOL2 = zerolist(20)

for i in range(20):
  for j in range(20):
    if a33 < PM_C[j][i]:
      a33 = PM_C[j][i]
  for j in range(20):
    if PM_C[j][i] == a33:
      a44+=1
      LOL1[i][j] = 1
  print("Количество максимумов в столбце [",i,"] =",a44)
  for j in range(20):
    LOL1[i][j]/=a44
  LOL2[i] = a44
  a33 = 0
  a44 = 0

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print(LOL1)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a33 = 0

LOL3 = zeromatrix(20,20)

for i in range(20):
  a33 = LOL2[i]
  for j in range(20):
    if LOL1[i][j]!=0:
      LOL3[i][j] = bernoulli.rvs(1/a33)
      a33-=1
    if LOL3[i][j]:
      break
      
print(LOL3)
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for i in range(20):
  for j in range(20):
    if LOL3[i][j]:
      print("M[",np.around(j,4),"] => C[",i,"]")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a33 = 0
a44 = 0

for i in range(20):
  for j in range(20):
    a33+=PM_C[j][i]*LOL1[i][j]
  a44 += (1 - a33)*PC[i]
  a33 = 0
print(a44)
