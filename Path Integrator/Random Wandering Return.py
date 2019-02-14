import matplotlib.pyplot as plt
import numpy as np

trialRes = [];
success = 0;

for i in range(0, 1000):
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
    #print(food_x, food_y)

    # if already within 10mm radius
    if (abs(x[-1]) < 10) and (abs(y[-1]) < 10):
        trialRes.append(1);
        # print(trialRes)
    else: # has 1 hour to get back in 10mm radius
        xval = np.random.normal(mean, std, steps)
        yval = np.random.normal(mean, std, steps)
        for i in range(0,steps):
            x.append(x[-1]+xval[i])
            y.append(y[-1]+yval[i])
            if (abs(x[-1]) < 10) and (abs(y[-1]) < 10):
                trialRes.append(1);
                # print("Got back in time so +1 to success.")
                # print(x[-1],y[-1]);
                # print(trialRes)
                break;
        if (abs(x[-1]) > 10) or (abs(y[-1]) > 10):
            trialRes.append(0)
            #print(trialRes)

for i in range(0, len(trialRes)):
    if trialRes[i] == 1:
        success = success + 1;

print(success)       # successes
print(len(trialRes)) # total trials
print(success/len(trialRes))
