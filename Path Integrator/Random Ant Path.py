import matplotlib.pyplot as plt
import numpy as np

x, y = [0],[0]
mean, std = 0, 1.0
steps = 60*60

xval = np.random.normal(mean, std, steps)
yval = np.random.normal(mean, std, steps)

for i in range(0,steps):
    x.append(x[-1]+xval[i])
    y.append(y[-1]+yval[i])

plt.suptitle('Ant Path over the Course of an Hour', fontsize=20)
plt.xlabel('X, Horizontal Distance Away from Nest (mm)', fontsize=16)
plt.ylabel('Y, Vertical Distance Away from Nest (mm)', fontsize=16)

plt.plot(x,y)
plt.show()
