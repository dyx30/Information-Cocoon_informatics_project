import numpy as np
import math
import matplotlib.pyplot as plt

Type=[0,0,1,1,2,3,3,3]

def cal_entro(P):

    p=[0 for i in range(4)]

    for i in range(8):
        p[Type[i]]+=P[i]

    entro=0
    for i in p:
        if i==0:
            continue
        entro-=i*math.log2(i)

    return entro

# P=[1/8,1/8,1/8,1/8,1/4,1/12,1/12,1/12]
# P=[1/3,1/6,0,0,1/2,0,0,0]
# print(cal_entro(P))