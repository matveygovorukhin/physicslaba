from matplotlib import pyplot as plt
from math import pi as pi
import numpy as np
from textwrap import wrap
import matplotlib.ticker as ticker
m=[1084.1, 481.0, 480.4, 487.2, 487.4, 331.0]
f=[0]*(len(m)+1)
for i in range(1, len(m)+1):
    for k in range(i):
        f[i]+=m[k]
    f[i]=f[i]/1000*9.81
F=f[-1]

nu=[161.2, 161.7, 162.2, 162.7, 163.2, 163.5, 164.0, 164.5, 165.0]
amp=[6, 8, 13, 32, 100, 21, 11, 7, 6]

fig, ax=plt.subplots()
ax.scatter(nu, amp)
z=np.polyfit(nu, amp, 45)
pol=np.poly1d(z)
# ax.plot(nu, y)
x=[i/100 for i in range(16120, 16500)]
# apr=[0.3171*(i**5)-248.6*(i**4)+77830*(i**3)-1.216*(10**7)*(i**2)+9.486*(10**8)*i-2.953*(10**10) for i in x]
y=pol(nu)
ax.plot(nu, y)

print(pol)
ax.set_xlabel("nu, Hz")
ax.set_ylabel("A, mV")
ax.set_title('зависимость амплитуды от частоты при близости к первому резонансу', loc = 'center')

ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

# plt.savefig('nu(n, m)')
# plt.savefig('achh')
plt.show()

