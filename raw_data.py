import json
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.records import array

with open("training data/x_acce_nopothole.txt", "r") as fp:
        a = json.load(fp)

with open("training data/y_acce_nopothole.txt", "r") as fp:
        b = json.load(fp)

with open("training data/z_acce_nopothole.txt", "r") as fp:
        c = json.load(fp)

with open("training data/time_nopothole.txt", "r") as fp:
        time = json.load(fp)

#Graphing to analyse our data acce pothole
fig, axs = plt.subplots(3)
fig.tight_layout(pad=3.0)


index = 25 #numero de bache sobre el cual trabajar
start = 0 #inicio de la ventana
finish = 0 #final de la ventana
print("LARGO " + str(len(a[index])))

axs[0].plot(time[index][start:finish],a[index][start:finish],'tab:blue')
axs[0].set_title('X')

axs[1].plot(time[index][start:finish],b[index][start:finish],'tab:red')
axs[1].set_title('Y')

axs[2].plot(time[index][start:finish],c[index][start:finish],'tab:green')
axs[2].set_title('Z')

arrayA = []
for i in range(0,15):
    arrayA.append(a[index][start+i])

arrayB = []
for i in range(0,15):
    arrayB.append(b[index][start+i])

arrayC = []
for i in range(0,15):
    arrayC.append(c[index][start+i])

arrayTime = []
for i in range(0,15):
    arrayTime.append(time[index][start+i])


arrayVentana = [arrayA, arrayB, arrayC, arrayTime]
print(arrayVentana)


for ax in axs:
    ax.set(xlabel='Time', ylabel='Value')

plt.show()