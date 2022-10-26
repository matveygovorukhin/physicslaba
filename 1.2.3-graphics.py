from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
time2=[]
with open('time.txt') as f:
    for l in f:
        time2.append(float(l)**2)
h=[0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.055, 0.065, 0.075]
# for i in h:
#     i=i**2
k=4.42/10000
m_razr=1536.3
m_pf=983.2
r=0.05
I_platf=8.57
I_prak=[k*(m_pf+m_razr)*(i) for i in time2]
I_teor=[ (m_razr*(r**2)/2 +m_razr*(i**2)+ I_platf) for i in h]

fig, ax=pyplot.subplots()
ax.scatter(time2, I_prak, c='blue', linewidth=0.5, label = 'практич')
ax.scatter(time2, I_teor, c='green', linewidth=0.5, label = 'теоретич')



ax.legend(shadow = False, loc = 'right', fontsize = 10)
ax.set_ylabel("момент импульса, г*м^2")
ax.set_xlabel("период, с")
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.axis([min(time2), max(time2)+1, min(I_prak), max(I_prak)+1])
pyplot.show()
