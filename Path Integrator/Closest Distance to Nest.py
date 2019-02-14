import matplotlib.pyplot as plt
import numpy as np

closestD = [];

for i in range(0, 1000):
    d= [];
    x, y = [0],[0] # as nest and starting point
    mean, std = 0, 1.0
    steps = 60*60

    xval = np.random.normal(mean, std, steps)
    yval = np.random.normal(mean, std, steps)

    for i in range(0,steps):
        x.append(x[-1]+xval[i])
        y.append(y[-1]+yval[i])

    food_x = x[-1];
    food_y = y[-1];
    # found food loc is food_x, food_y
    # print(food_x, food_y)

    # continuing to walk randomly
    xval = np.random.normal(mean, std, steps)
    yval = np.random.normal(mean, std, steps)

    for i in range(0,steps):
        x.append(x[-1]+xval[i])
        y.append(y[-1]+yval[i])
        d.append(np.sqrt(x[-1]**2 + y[-1]**2))
    closestD.append(min(d))

print(sum(closestD)/len(closestD))
