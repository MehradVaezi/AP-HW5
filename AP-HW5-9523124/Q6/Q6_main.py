import math
import subprocess
from time import time as epochTime
import matplotlib.pyplot as plt
import numpy as np
import PGaussSolver as PyGauss


def aFunction(x):
    xN = 0.5*x+0.5
    return (((xN**3)/(xN+1))*(math.cos(xN**2)))




a = 0
b = 1
P_time = []
C_time = []
N = 20
for n in range(1, N+1):

	# Python Code Running...
    Pstart = epochTime()
    aSolver = PyGauss.PGaussSolver(aFunction, a, b, n)
    aSolver.execute()
    print(f"Result of Python code (n = {n}): {aSolver.getResult()}")
    Pstop = epochTime()
    P_time.append(round((Pstop - Pstart), 4))

    print(f"Python Code took: {Pstop - Pstart} seconds...", '\n')

    # C++ Code Running...
    Cstart = epochTime()
    subprocess.call(["IntegrateC++.exe", str(n)])
    Cstop = epochTime()
    C_time.append(round((Cstop - Cstart), 4))

    print(f"C++ Code took: {Cstop - Cstart} seconds...")
    print("="*30)

# Drawing Table... (Matplotlib)
data = [[i for i in range(1, N+1)], C_time[:], P_time[:]]
fig, axs = plt.subplots(2, 1)
rowlabel = ("N", "C++", "Python")
axs[0].axis('tight')
axs[0].axis('off')
the_table = axs[0].table(cellText=data, rowLabels=rowlabel, loc = 'center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)
fig.suptitle("C++ / Python Runtime Comparison")
axs[1].set(xlabel="Legendre Degree (n)", ylabel="Runtime [s]")
axs[1].plot(data[0], data[1], label = "C++")
axs[1].plot(data[0], data[2], label = "Python")
axs[1].legend(loc = "upper center")
plt.grid('True')

plt.show()
