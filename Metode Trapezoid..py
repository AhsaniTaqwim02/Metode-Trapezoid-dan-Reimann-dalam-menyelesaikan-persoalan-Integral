import numpy as nmp
import matplotlib.pyplot as plt

#Memasukan fungsi eksponensial sesuai soal
def func(x):
return (x**2)*nmp.exp(-x)

# Data yang dimasukan dalam n = 10,100, dan 1000 Manual dalam program 
a = 1.0
b = 10.0
n = 1000

# # Rumus Metode Trapezoid yang digunakan
dx = (b-a)/(n-1)
x = nmp.linspace(a,b,n)
sigma = 0
for i in range (1, n-1):
    sigma += func(x[i])
hasil = 0.5*dx*(func(x[0])+2*sigma+func(x[-1]))
print (hasil)

xp =nmp.linspace(a,b)
plt.plot(xp,func(xp))

# Variasi warna dan bentuk grafik yang ingin dihasilkan
for i in range (n):
    plt.bar(x[i],func(x[i]), align = 'edge', width = 0.0001, color = 'blue', edgecolor = 'green')


plt.fill_between(x,func(x),color= 'cyan')
plt.show()
