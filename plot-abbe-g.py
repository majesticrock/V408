import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x +b

werte = csv_read("csv/abbe.csv")
xdata = np.zeros(10)
ydata = np.zeros(10)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        ydata[i] = float(values[1])
        xdata[i] = 1 + (1 /( float(values[3]) / 3))
        
        i+=1

x_line = np.linspace(np.amin(xdata), np.amax(xdata))
plt.plot(xdata, ydata, 'bx', label="Wertepaare")
popt1, pcov1 = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt1), "r-", label="Ausgleichsgerade")
plt.xlabel(r"$1 + \frac{1}{V}$")
plt.ylabel(r"$g$ / cm")

print(popt1)
print(np.sqrt(np.diag(pcov1)))

plt.legend()
plt.tight_layout()
plt.savefig("build/plot_abbe_g.pdf")