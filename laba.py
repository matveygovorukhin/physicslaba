from matplotlib import pyplot
import matplotlib.ticker as mtick
from matplotlib.ticker import PercentFormatter
import numpy
import math

with open('270.txt') as file:
    lst = list(map(float,file.readline().split()))
lst.sort()
R_sr=numpy.mean(lst)
sum2=0
for i in range(270):
    sum2+=(lst[i]-R_sr)**2
sigma=(sum2/270)**0.5
print(sigma)
y=[]
for i in range(270):
    y.append((math.e**(-(lst[i]-R_sr)**2/2*sigma**2))/(sigma*(2*math.pi)**0.5))

fig, ax = pyplot.subplots(figsize=(7, 7))
ax.plot(lst, y)
ax.hist(lst, 40, density=True,facecolor='g', alpha=0.75)
pyplot.xlabel('сопротивление R, Ом')
pyplot.ylabel('плотность вероятности, ω')


fig, bx = pyplot.subplots(figsize=(7, 7))
bx.plot(lst, y)
bx.hist(lst,30,density=True,facecolor='g', alpha=0.75)
pyplot.xlabel('сопротивление R, Ом')
pyplot.ylabel('плотность вероятности, ω')

pyplot.show()

