from matplotlib import pyplot as plt
from math import pi as pi
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker
m=[1084.1, 481.0, 480.4, 487.2, 487.4, 331.0]
nu=[1, 2, 3, 4, 5, 6, 7, 8, 9]
n0=[93.1, 138.3, 283.3, 378.2, 473.1, 567.9, 663.5, 759.4, 855.3]
n1=[111.7, 225.7, 338.2, 451.8, 563.9, 679.2, 791.1, 907.9, 1019.6]
n2=[127.9, 258.0, 386.2, 516.7, 644.5, 775.3, 903.7, 1034.6, 1163.5]
n3=[141.6, 285.8, 426.7, 571.5, 714.2, 857.7, 1000.8, 1145.6, 1287.6]
n4=[154.7, 310.4, 466.1, 623.1, 777.8, 934.5, 1088.7, 1247.2, 1401.2]
n5=[163.1, 327.0, 491.5, 654.3, 819.3, 983.2, 1148.1, 1312.1, 1477.2]

f=[0]*(len(m)+1)
for i in range(1, len(m)+1):
    for k in range(i):
        f[i]+=m[k]
    print(f[i])
    f[i]=f[i]/1000*9.81
f=f[1:]
fig, ax=plt.subplots()

# ax.scatter(nu, n0)
# z=numpy.polyfit(nu, n0, 1)
# pol=numpy.poly1d(z)
# y=pol(nu)
# ax.plot(nu, y, label = '$m_0$')
# print(pol)
#
# ax.scatter(nu, n1)
# z=numpy.polyfit(nu, n1, 1)
# pol=numpy.poly1d(z)
# y=pol(nu)
# ax.plot(nu, y, label = '$m_1$')
# print(pol)
#
# ax.scatter(nu, n2)
# z=numpy.polyfit(nu, n2, 1)
# pol=numpy.poly1d(z)
# y=pol(nu)
# ax.plot(nu, y, label = '$m_2$')
# print(pol)
#
# ax.scatter(nu, n3)
# z=numpy.polyfit(nu, n3, 1)
# pol=numpy.poly1d(z)
# y=pol(nu)
# ax.plot(nu, y, label = '$m_3$')
# print(pol)
#
# ax.scatter(nu, n4)
# z=numpy.polyfit(nu, n4, 1)
# pol=numpy.poly1d(z)
# y=pol(nu)
# ax.plot(nu, y, label = '$m_4$')
# print(pol)
#
# ax.scatter(nu, n5)
# z=numpy.polyfit(nu, n5, 1)
# pol=numpy.poly1d(z)
# y=pol(nu)
# ax.plot(nu, y, label = '$m_5$')
# print(pol)
#
# ax.set_xlabel("n")
# ax.set_ylabel("nu, Гц")
# ax.legend(shadow = False, loc = 'upper left', fontsize = 15)
# ax.set_title('зависимость частоты от числа полуволн и массы грузов', loc = 'center')

v2=[143.814, 167.072, 190.477, 210.938, 229.485, 241.702]
for i in range(6):
    v2[i]=v2[i]**2
ax.scatter(f, v2)
z=numpy.polyfit(f, v2, 1)
pol=numpy.poly1d(z)
y=pol(f)
ax.plot(f, y, c='green')
print(pol)
p = interp_naive(x, y)
print(numpy.linalg.norm(p-y))
ax.set_xlabel("F, H")
ax.set_ylabel("$V^2, m^2/c^2$")
ax.set_title('зависимость квадрата скоррости от силы веса грузиков', loc = 'center')

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

# plt.savefig('nu(n, m)')
plt.savefig('v2(F)')
# plt.show()