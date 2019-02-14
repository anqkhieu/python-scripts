
import matplotlib.pyplot as plt

# edit vars
numTrials = 125

plt.suptitle('Alternating Pairing Bell-Food Trials and Bell-NoFood Extinction Trials', fontsize=20)
plt.xlabel('Trial Number', fontsize=16)
plt.ylabel('Association Strength for Bell and Food', fontsize=16)

l = 1.0;
a = 0.75; # var
b = 0.1; # var

V = 0.0; # init assoc strength
trialVals = [];
trialNum = list(range(0, numTrials+1))
trialVals.append(V)

for i in range(1, numTrials+1):
    if (i % 2 == 1) :
        dV = a * b * (1-V)
        V = V + dV;
        trialVals.append(V)
    if (i % 2 == 0):
        dV = a * b * (-V)
        V = V + dV;
        trialVals.append(V)

plt.plot(trialNum, trialVals)
plt.show()
