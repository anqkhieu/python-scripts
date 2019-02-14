import matplotlib.pyplot as plt
import numpy as np
import math

avgD, avgEnergy, d, energy, SVals = [], [], [], [], [];
S = 0; # set var to 0.0001mm

while S < 1:
    if (S == 0):
        S = 0.001;
    else:
        S = S + 0.01; # var from 0.001mm up to 1.0mm
        if (S > 1):
            S = 1;
    SVals.append(S);
    for i in range(0, 100):  # 100 trials
        mem_x, mem_y = [],[];
        x, y = [0],[0]
        mean, std = 0, 1.0
        steps = 60*60

        xval = np.random.normal(mean, std, steps)
        yval = np.random.normal(mean, std, steps)

        for i in range(0,steps):
            x.append(x[-1]+xval[i])
            y.append(y[-1]+yval[i])
            e_x = np.random.normal(0, scale=S);
            e_y = np.random.normal(0, scale=S);
            mem_x.append(xval[i] + e_x); # errored memory vector x
            mem_y.append(yval[i] + e_y); # errored memory vector y

        ant_x, ant_y = [x[-1]], [y[-1]];

        for i in range(0,steps):
            ant_x.append(ant_x[-1] - mem_x[-1-i]);
            ant_y.append(ant_y[-1] - mem_y[-1-i]);

        d.append(np.sqrt((ant_x[-1])**2 + (ant_y[-1])**2))
        energy.append(math.exp(0.1/S) + d[-1]**2)

    avgD.append(sum(d)/len(d))
    avgEnergy.append(sum(energy)/len(energy))
    d, energy = [], [];
    # print(S,avgD)

plt.suptitle('Ant Average Energy Expenditure VS Standard Deviation of Noise', fontsize=20)
plt.xlabel('Standard Deviation of Noise (mm)', fontsize=16)
plt.ylabel('Average Energy Unit Expenditure', fontsize=16)
plt.xscale("log")
plt.yscale("log")
plt.plot(SVals, avgEnergy)
print(min(avgEnergy))
minIndex = avgEnergy.index(min(avgEnergy))
print(SVals[minIndex])
plt.show();
