#import necessary libraries for python
import numpy as np
import matplotlib.pyplot as plt

#define basic variables for the model
N=10000
S=[9990]
I=[10]
R=[0]
Time=[0]
beta=0.3
gamma=0.05
#creating loops for 1000 times
for i in range(1,1000):
    Time.append(i)
    #calculating the population from infected to recovered in this loop
    lis_ItoR=np.random.choice(range(2),I[i-1],p=[gamma,1-gamma])
    ItoR=np.sum(lis_ItoR==0)
    proportion=I[i-1]/N
    Pinfect=proportion*beta
    #cauculating the population from susceptible to infected
    lis_StoI=np.random.choice(range(2),S[i-1],p=[1-Pinfect,Pinfect])
    StoI=np.sum(lis_StoI==1)
    #append the new values in the arrays
    I.append(I[i-1]-ItoR+StoI)
    R.append(R[i-1]+ItoR)
    S.append(S[i-1]-StoI)

#draw graph for the SIR model
plt.figure()
plt.figure(figsize =(6,4),dpi=150)
plt.title('SIR model')
plt.plot(Time,S,label='Susceptible')
plt.plot(Time,I,label='Infected')
plt.plot(Time,R,label='Recovered')
plt.xlabel('Time')
plt.ylabel('population')
plt.legend()
plt.show()
plt.clf()