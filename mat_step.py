import numpy as np
import math
import matplotlib.pyplot as plt

Type=[0,0,1,1,2,3,3,3]
Count=[2,2,2,2,1,3,3,3]

def mat_step(cls):

    global transmat

    for i in range(8):
        for j in range(8):
            if Type[j]==Type[cls]:
                continue
            transmat[i][j]/=2.0
    
    tmp=[]
    for i in range(8):
        tmp.append(1.0-np.sum(transmat[i,:]))

    for i in range(8):
        for j in range(8):
            if j==cls:
                transmat[i][j]+=tmp[i]*(2.0/(Count[i]+1))
            elif Type[j]==Type[cls]:
                transmat[i][j]+=tmp[i]*(1.0/(Count[i]+1))

transmat = np.random.rand(8, 8)
for i in range(8):
    norm=np.sum(transmat[i,:])
    for j in range(8):
        transmat[i][j]/=norm

# print(transmat)
# for i in range(2):
#     mat_step(1)
#     print(transmat)