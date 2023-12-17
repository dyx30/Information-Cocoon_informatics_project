import numpy as np
import math
import matplotlib.pyplot as plt

def entro_plot(x):
    plt.plot(x)
    plt.title('Trend of entropy change')
    plt.xlabel('Iterations')
    plt.ylabel('Entropy / bit')
    plt.show()

# x=[2,1.5,1.6,1,0.8,0.5,0.2,0.18,0.16,0.15,0.14,0.14]
# entro_plot(x)