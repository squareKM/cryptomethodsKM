import pandas as pd
import numpy as np

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
for i in range(0,20,1): 
  for j in range(0,20,1):
    for k in range(0,20,1):
      CM_finder(i,j,k,PC)

print(PC)
aa = 0
for i in range(0,20,1):
  aa += PC[i]

print("TEST =",aa)

def CM_finder1(x,y,z,q):
  if table_array[x][y] == z:
    q[y][z] += prob_array[0][y] * prob_array[1][x]

PMC = zeromatrix(20,20)

for i in range(0,20,1): 
  for j in range(0,20,1):
    for k in range(0,20,1):
      CM_finder1(i,j,k,PMC)

print(PMC)
aa = 0
for i in range(0,20,1): 
  for j in range(0,20,1):
    aa += PMC[i][j]

print("TEST =",aa)

PM_C = PMC

for i in range(0,20,1): 
  for j in range(0,20,1):
    PM_C[i][j] = PM_C[i][j]/PC[j]

print(PM_C)