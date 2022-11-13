from matplotlib import pyplot as plt
from math import pi as pi
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
data_time=[]
with open('data_time.txt') as f:
    for l in f:
        data_time.append(float(l))
data_h=[]
with open('data_h.txt') as f:
    for l in f:
        data_h.append(int(l)/1000)
data_h2=[i**2 for i in data_h]
data_time2=[i**2 for i in data_time]

fig, ax=plt.subplots()
ax.scatter(data_h2, data_time2, 15, c='red', linewidth=0.02)
z=numpy.polyfit(data_h2, data_time2, 1)
p=numpy.poly1d(z)
y=p(data_h2)
print(p)
# ax.plot(data_h2, data_time2, c='green', linewidth=0.2)
k=788.4
b=1.488
mas_x=[i/(10**6) for i in range(2800, 17800)]
mas=[(k*i+b) for i in mas_x]
ax.plot(mas_x, mas, linewidth=1)
# print(data_h2)
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.005))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.001))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.axis([0, max(data_h2)+0.001, 0, max(data_time2)+1])
ax.set_xlabel("h, м^2")
ax.set_ylabel("T, с^2")

plt.show()
