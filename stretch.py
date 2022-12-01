from matplotlib import pyplot as plt
from math import pi as pi
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
m1=[]
with open('m_stretch.txt') as f:
    for l in f:
        m1.append(float(l)/1000)
m=[0]*(len(m1)+1)
for i in range(1, len(m1)+1):
    for k in range(i):
        m[i]+=m1[k]

y_up=[]
with open('y_up_stretch.txt') as f:
    for l in f:
        y_up.append(int(l)/1000)
y_down=[]
with open('y_down_stretch.txt') as f:
    for l in f:
        y_down.append(int(l)/1000)

d=0.00051
r=0.02
l=1.740
h=1.344
g=9.81
# y=[]
# for i in range(len(y_up)):
#     y.append((y_up[i]+y_down[len(y_up)-i-1])/2)
p1=[m[i]*g for i in range(len(m))]
p=[]
for i in range(len(p1)):
    p.append(p1[i])
    p.append(p1[i])
y_down.reverse()
# print(y_up)
# print(y_down)
l0_up=y_up[0]*r/(2*h)
l0_down=y_down[0]*r/(2*h)
delta_l_up=[ y_up[i]*r/(2*h) - l0_up for i in range(1, len(y_up))]
delta_l_down=[ y_down[i]*r/(2*h) - l0_down for i in range(1, len(y_up))]
delta_l=[0]*2
for i in range(len(delta_l_down)):
    delta_l.append(delta_l_up[i])
    delta_l.append(delta_l_down[i])

fig, ax=plt.subplots()
delta_l[0]=l0_up
delta_l[1]=l0_down
ax.scatter(p[2:], delta_l[2:], 10)

z=numpy.polyfit(p[6:], delta_l[6:], 1)
pol=numpy.poly1d(z)
y=pol(p)
print(pol)
print(p)
k=0.00004822
b=0.00003478

y_pol=[k*i+b for i in p]
ax.plot(p, y_pol, c='green', linewidth=1)
# ax.plot(p, pol)

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.0001))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.00002))
ax.axis([0, max(p)+1, 0, max(delta_l)+0.0001])
ax.set_xlabel("p, H")
ax.set_ylabel("delta L, m")

# print(p)
# print(delta_l)

plt.show()