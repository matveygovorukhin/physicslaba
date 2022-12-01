from matplotlib import pyplot
x=[i*0.001 for i in range(-2000, 2100)]
y=[(1-i**2/4)**0.5 for i in x]
x1=[i*0.001 for i in range(-2000, 2100)]
y1=[-(1-i**2/4)**0.5 for i in x]
pyplot.plot(x, y)
pyplot.plot(x1, y1)
pyplot.show()