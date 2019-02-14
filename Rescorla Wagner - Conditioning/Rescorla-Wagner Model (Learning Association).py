
import matplotlib.pyplot as plt
# to change figure size:
# import matplotlib as mpl
# mpl.rcParams['figure.figsize'] = (10,10)

plt.suptitle('Paired Light and Food in 13 Trials to surpass a 0.8 Learning Association', fontsize=20)
plt.xlabel('Trial Number', fontsize=16)
plt.ylabel('Association Strength', fontsize=16)

l = 1.0;
b = 0.1;
a = 0.0;     # temp set

V = 0.05;
trialVals = [V];
trialNum = list(range(0, 14))

while trialVals[-1] <= 0.8:
    a = a + 0.01;
    V = 0.05;
    trialVals = [V];
    for i in range(13):
        dV = a * b * (1-V)
        V = V + dV;
        trialVals.append(V)
    if trialVals[-1] > 0.8:
        print(a)
        break

print(trialVals)
print(trialNum)

plt.plot(trialNum, trialVals)
plt.show()
