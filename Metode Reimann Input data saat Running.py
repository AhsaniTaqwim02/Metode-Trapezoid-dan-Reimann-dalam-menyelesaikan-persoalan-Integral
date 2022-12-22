import numpy as p
import matplotlib.pyplot as plt

#Memasukan fungsi eksponensial sesuai soal
def func(x):
return (x**2)*p.exp(-x)

#Data yang dimasukan dalam n = 10,100, dan 1000 Manual dalam program 
a = 1.0
b = 10.0
n = int (input('n = ')) # n diubah sesuai kebutuhan

# Rumus Metode reimann yang digunakan
x = p.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0

for i in range (n-1):
    hasil += dx*func(x[i])
print('Hasil = ', hasil)

xp = p.linspace(a,b)
plt.plot(xp,func(xp))
# Variasi warna dan bentuk grafik yang ingin dihasilkan
for i in range(n-1):
    plt.bar(x[i],func(x[i]), align = 'edge',width=dx, color='red',edgecolor='black')
plt.show()
