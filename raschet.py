from matplotlib import pyplot
from math import pi
x0=[2.5**2]
y0=[2.5**2/(4*pi**2)]
xk=[9]
yk=[9/4/pi**2-y0[0]]
xx=[4**2]
xy=[3.8**2]
xz=[3.2**2]
yx=[16/4/pi**2-y0[0]]
yy=[3.8**2/4/pi**2-y0[0]]
yz=[3.2**2/4/pi**2-y0[0]]
xp=[3.3**2]
yp=[3.3**2/4/pi**2-y0[0]]
xe=[3.4**2]
ye=[3.4**2/4/pi**2-y0[0]]
xd=[3.5**2]
yd=[3.5**2/4/pi**2-y0[0]]
xd1=[3.2**2]
yd1=[3.2**2/4/pi**2-y0[0]]
xh1=[9]
yh1=[9/4/pi**2-y0[0]]
xh2=[3.1**2]
yh2=[3.1**2/4/pi**2-y0[0]]
pyplot.xlabel('T^2')
pyplot.ylabel('I')
pyplot.scatter(x0, y0)
pyplot.scatter(xk, yk, c='red')
pyplot.scatter(xx, yx, c='green')
pyplot.scatter(xy, yy, c='green')
pyplot.scatter(xz, yz, c='green')
pyplot.scatter(xp, yp, c='green')
pyplot.scatter(xe, ye, c='green')
pyplot.scatter(xd, yd, c='green')
pyplot.scatter(xh1, yh1, c='purple')
pyplot.scatter(xd1, yd1, c='purple')
pyplot.scatter(xh2, yh2, c='black')
pyplot.show()