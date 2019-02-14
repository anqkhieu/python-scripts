import matplotlib.pyplot as plt
import numpy as np

avgD, d, SVals = [], [], [];
S = 0; # set var to 0.0001mm

while S < 1:
    if (S == 0):
        S = 0.001; # set var to 0.0001mm
    else:
        S = S + 0.2; # var from 0.0001mm up to 1.0mm
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

    avgD.append(sum(d)/len(d))
    d = [];
    print(S,avgD)


plt.suptitle('Standard Deviation of Noise VS Average Distance from Nest', fontsize=20)
plt.xlabel('Standard Deviation of Noise (mm)', fontsize=16)
plt.ylabel('Average Distance from Nest (mm)', fontsize=16)
plt.plot(SVals, avgD)
plt.xscale("log")
plt.show();
