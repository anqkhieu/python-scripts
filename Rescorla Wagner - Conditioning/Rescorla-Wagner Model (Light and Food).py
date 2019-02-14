
import matplotlib.pyplot as plt

plt.suptitle('Paired Light and Food (Rescorla-Wagner Model) with 0.05 initial association', fontsize=20)
plt.xlabel('Trial Number', fontsize=16)
plt.ylabel('Association Strength', fontsize=16)

l = 1.0;
a = 0.75;
b = 0.1;

# First Graph, 20 Trials
V = 0.05;
trialVals = [];
trialNum = list(range(0, 21))
trialVals.append(V)

for i in range(20):
    dV = a * b * (1-V)
    V = V + dV;
    trialVals.append(V)

plt.plot(trialNum, trialVals)
plt.show()

print(len(trialVals))
print(len(trialNum))

# Second Graph, 20 Trials
plt.suptitle('Paired Light and Food (Rescorla-Wagner Model) with 0.5 initial association', fontsize=20)
plt.xlabel('Trial Number', fontsize=16)
plt.ylabel('Association Strength', fontsize=16)

V = 0.5;
trialVals = [];
trialNum = list(range(0, 21))
trialVals.append(V)

for i in range(20):
    dV = a * b * (1-V);
    V = V + dV;
    trialVals.append(V)

plt.plot(trialNum, trialVals)
plt.show()
