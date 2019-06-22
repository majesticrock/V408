import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *


def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def average(content):
    first_index=0
    n=len(content)
    avg=0
    for i in range(first_index, n):
        avg += content[i]
    
    avg /= (n-first_index)

    for i in range(first_index, n):
        avg_err = (content[i] - avg)**2

    avg_err = np.sqrt(avg_err)
    avg_err /= np.sqrt((n-first_index) * (n-1-first_index))

    return [avg, avg_err]

con = csv_read("csv/schnittpunkt.csv")
B = np.zeros(10)
b = np.zeros(10)
g = np.zeros(10)
V = np.zeros(10)
v = np.zeros(10)


ignore = True
i=0
for value in con:
    if(ignore):
        ignore = False
    else:
        B[i] = float(value[2])
        b[i] = float(value[1])
        g[i] = float(value[0])
        i+=1


V = B / 3.0 #cm
for i in range(0, 10):
    v[i] = b[i] / g[i]


print("V:")
print(V)
print(v)
print("----------------------------------------")

diff = np.zeros(10)
for i in range(0, 10):
    diff[i] = abs(V[i] - v[i])/V[i]

avg_diff = average(diff)

print("Diff V:")
print(diff)
print(avg_diff)
print("----------------------------------------")


f = np.zeros(10)

for i in range(0, 10):
    f[i] = (1/b[i]) + (1/g[i])
    f[i] = (1/f[i])


f_avg = average(f)


print("f:")
print(f)
print(f_avg)
print("----------------------------------------")

#Bessel

con = csv_read("csv/bessel.csv")
e  = np.zeros(10) 
g1 = np.zeros(10)
b1 = np.zeros(10)
g2 = np.zeros(10)
b2 = np.zeros(10)

ignore = True
i=0

for val in con:
    if(ignore):
        ignore=False
    else:
        e[i]  = float(val[0])
        g1[i] = float(val[1])
        b1[i] = float(val[2])
        g2[i] = float(val[3])
        b2[i] = float(val[4])
        i+=1

mittel_1 = np.zeros(10)
mittel_2 = np.zeros(10)
d=np.zeros(10)
f=np.zeros(10)


for i in range(0,10):
    mittel_1[i] = 0.5 * ( g2[i] + b1[i] )
    mittel_2[i] = 0.5 * ( g1[i] + b2[i] )
    d[i] = mittel_1[i] - mittel_2[i]
    f[i] = ( e[i]**2 - (mittel_1[i] - mittel_2[i])**2) / (4*e[i])

f_avg = average(f)

print("g/b mittel:")
print(d)
print(f)
print(f_avg)
print("----------------------------------------")

