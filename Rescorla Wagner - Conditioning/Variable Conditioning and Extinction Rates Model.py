
import matplotlib.pyplot as plt
import pylab
import random

numTrials = 200

# edit vars

P = 1

plt.suptitle('Different Probabilities Pairing Bell-Food or Bell-No Food Extinction', fontsize=20)
plt.xlabel('Trial Number', fontsize=16)
plt.ylabel('Association Strength for Bell and Food', fontsize=16)

l = 1.0;
a = 0.75; # var
b = 0.1; # var

V = 0.0; # init assoc strength
trialVals = [];
trialNum = list(range(0, numTrials+1))
trialVals.append(V)

for i in range(numTrials):
    randN =  random.random()
    if randN <= P:
        dV = a * b * (1-V)
        V = V + dV;
        trialVals.append(V)
    else: # all other cases lie in (1-P)
        dV = a * b * (-V)
        V = V + dV;
        trialVals.append(V)

plt.plot(trialNum, trialVals, label='P = 1')

#

P = 0.75

l = 1.0;
a = 0.75; # var
b = 0.1; # var

V = 0.0; # init assoc strength
trialVals = [];
trialNum = list(range(0, numTrials+1))
trialVals.append(V)

for i in range(numTrials):
    randN =  random.random()
    if randN <= P:
        dV = a * b * (1-V)
        V = V + dV;
        trialVals.append(V)
    else: # all other cases lie in (1-P)
        dV = a * b * (-V)
        V = V + dV;
        trialVals.append(V)

plt.plot(trialNum, trialVals, label='P = 0.75')

#
P = 0.50

l = 1.0;
a = 0.75; # var
b = 0.1; # var

V = 0.0; # init assoc strength
trialVals = [];
trialNum = list(range(0, numTrials+1))
trialVals.append(V)

for i in range(numTrials):
    randN =  random.random()
    if randN <= P:
        dV = a * b * (1-V)
        V = V + dV;
        trialVals.append(V)
    else: # all other cases lie in (1-P)
        dV = a * b * (-V)
        V = V + dV;
        trialVals.append(V)

plt.plot(trialNum, trialVals, label='P = 0.5')


#

P = 0.25

l = 1.0;
a = 0.75; # var
b = 0.1; # var

V = 0.0; # init assoc strength
trialVals = [];
trialNum = list(range(0, numTrials+1))
trialVals.append(V)

for i in range(numTrials):
    randN =  random.random()
    if randN <= P:
        dV = a * b * (1-V)
        V = V + dV;
        trialVals.append(V)
    else: # all other cases lie in (1-P)
        dV = a * b * (-V)
        V = V + dV;
        trialVals.append(V)

plt.plot(trialNum, trialVals, label='P = 0.25')
plt.legend()
plt.show()
