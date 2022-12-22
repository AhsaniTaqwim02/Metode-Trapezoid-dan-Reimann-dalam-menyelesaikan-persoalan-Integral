import numpy as nmp
import matplotlib.pyplot as plt
def func(x):
return (x**2)*nmp.exp(-x)

#Data yang dimasukan dalam n = 10,100, dan 1000 Manual dalam program 
a = 1.0
b = 10.0
n = 10

x = nmp.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0

for i in range(n-1):
    hasil += dx*func(x[i])
print (hasil)

xp=nmp.linspace(a,b)
plt.plot(xp,func(xp))
for i in range(n-1):
        plt.bar(x[i],func(x[i]), align ='edge', width=dx, color='azure', edgecolor='black')
plt.show()
