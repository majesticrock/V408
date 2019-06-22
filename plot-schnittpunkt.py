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

def func(x, a, b):
    return a*x + b

n=10
werte = csv_read("csv/schnittpunkt.csv")
a = np.zeros(n)
b = np.zeros(n)
x = np.zeros(n)

ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        b[i] = float(values[1])
        a[i] = - b[i] / float(values[0])
        x[i] = float(values[0])
        i+=1

plt.figure(1)
plt.grid(True)

for i in range(0, n):
    xdata=np.linspace(0, x[i])
    plt.plot(xdata, func(xdata, a[i], b[i]), "r-", linewidth=0.4)


plt.xlabel(r"$g$ / cm")
plt.ylabel(r"$b$ / cm")
#plt.legend()
plt.tight_layout()
plt.savefig("build/plot_schnittpunkt.pdf")

plt.figure(2)

plt.grid(True)

for i in range(0, n):
    xdata=np.linspace(7, 13)
    plt.plot(xdata, func(xdata, a[i], b[i]), "r-", linewidth=0.4)


plt.xlabel(r"$g$ / cm")
plt.ylabel(r"$b$ / cm")
#plt.legend()
plt.tight_layout()
plt.savefig("build/plot_schnittpunkt_zoom.pdf")