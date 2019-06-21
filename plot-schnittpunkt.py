import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

#Gegenstandsgröße = 3cm

n=10
werte = csv_read("csv/schnittpunkt.csv")
xdata = np.zeros(n)
ydata = np.zeros(n)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[1])
        i+=1

plt_arr = np.array([0,0])
plt_arr2 = np.array([0,0])

plt.grid(True)

for i in range(0, n):
    plt_arr[0] = xdata[i]
    plt_arr2[1] = ydata[i]
    plt.plot(plt_arr, plt_arr2, "r-", linewidth=0.5)


plt.xlabel(r"$g$ / cm")
plt.ylabel(r"$b$ / cm")
#plt.legend()
plt.tight_layout()
plt.savefig("build/plot_schnittpunkt.pdf")