from matplotlib import pyplot as plt
from math import pi as pi
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
m_bend=[]
with open('m_bend.txt') as f:
    for l in f:
        m_bend.append(float(l)/1000)

y_bend_wood_flat=[]
with open('y_bend_wood_flat.txt') as f:
    for l in f:
        y_bend_wood_flat.append(float(l)/1000)

y_bend_wood_edge=[]
with open('y_bend_wood_edge.txt') as f:
    for l in f:
        y_bend_wood_edge.append(float(l)/1000)

y_bend_metal=[]
with open('y_bend_metal.txt') as f:
    for l in f:
        y_bend_metal.append(float(l)/1000)

m=[0]*(len(m_bend)+1)
for i in range(1,  len(m_bend)+1):
    for k in range(i):
        m[i]+=m_bend[k]
weight=[]
for i in m:
    weight.append(i*9.81)
    weight.append(i*9.81)


fig, ax=plt.subplots()

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

# ax.scatter(weight, y_bend_wood_flat, 10)
# z=numpy.polyfit(weight, y_bend_wood_flat, 1)
# p=numpy.poly1d(z)
# y=p(weight)
# print(p)
# ax.plot(weight, y, c='green')
# ax.set_title('дерево плоскостью', loc = 'center')
# ax.set_xlabel("p, H")
# ax.set_ylabel("y, m")
# plt.savefig('wood_flat')

# ax.scatter(weight, y_bend_wood_edge)
# z=numpy.polyfit(weight, y_bend_wood_edge, 1)
# p=numpy.poly1d(z)
# y=p(weight)
# print(p)
# ax.plot(weight, y, c='green')
# ax.set_title('дерево ребром', loc = 'center')
# ax.set_xlabel("p, H")
# ax.set_ylabel("y, m")
# plt.savefig('wood_edge')

ax.scatter(weight, y_bend_metal)
z=numpy.polyfit(weight, y_bend_metal, 1)
p=numpy.poly1d(z)
y=p(weight)
print(p)
ax.plot(weight, y, c='green')
ax.set_title('металл', loc = 'center')
ax.set_xlabel("p, H")
ax.set_ylabel("y, m")
# plt.savefig('metal')
