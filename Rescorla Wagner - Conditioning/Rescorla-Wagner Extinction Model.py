
import matplotlib.pyplot as plt

# changing figure size
# import matplotlib as mpl
# mpl.rcParams['figure.figsize'] = (10,10)

# def V_bellfood_plotter(numTrials):

numTrials = 100;

plt.suptitle('Pairing Light and Food with a Bell (Blocking Rescorla-Wagner Model)', fontsize=16)
plt.xlabel('Trial Number', fontsize=16)
plt.ylabel('Association Strength for Bell and Food', fontsize=16)

l = 1.0;
a = 0.75;
b = 0.1;

# First Graph, 20 Trials
V_lightfood = 0.8;
V_bellfood = 0.0;
# V = V_lightfood + V_bellfood;

trialVals = [];
trialNum = list(range(0, numTrials+1))
trialVals.append(V_bellfood)

for i in range(numTrials):
    dV = a * b * (1-(V_lightfood+V_bellfood))
    V_lightfood = V_lightfood + dV;
    V_bellfood =  V_bellfood + dV;
    trialVals.append(V_bellfood)

plt.plot(trialNum, trialVals)
plt.show()



# import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.rcParams['figure.figsize'] = (10,10)
#
# def V_bellfood_plotter(numTrials):
#     plt.suptitle('Initial Association Strenght between Light and Food (0.8)', fontsize=16)
#     plt.xlabel('Trial Number', fontsize=16)
#     plt.ylabel('Association Strength between Bell and Food', fontsize=16)
#
#     l = 1.0;
#     a = 0.75;
#     b = 0.1;
#
#     # First Graph, 20 Trials
#     V_lightfood = 0.8;
#     V_bellfood = 0.0;
#     V = V_lightfood + V_bellfood;
#
#     trialVals = [];
#     trialNum = list(range(0, numTrials+1))
#     trialVals.append(V_bellfood)
#
#     for i in range(numTrials):
#         dV = a * b * (1-(V_lightfood+V_bellfood))
#         V_lightfood = V_lightfood + dV;
#         V_bellfood =  V_bellfood + dV;
#         trialVals.append(V_bellfood)
#
#     plt.plot(trialNum, trialVals)
#     plt.show()
#
