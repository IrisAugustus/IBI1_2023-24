#import necessary libraries for python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

plt.figure(figsize =(6,4),dpi=150)
plt.title('SIR model with different vaccination rates')
plt.xlabel('Time')
plt.ylabel('number of infected population')
#Set value for the percentage of people vaccinated
percentage=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
#plot infected population for every rate in the list
for rate in percentage:
    #define basic variables for the model, initialize for every rate
    N=10000
    S=[]
    I=[10]
    R=[0]
    Time=[0]
    beta=0.3
    gamma=0.05
    vaccinated_pop=rate*N
    unvaccinated_pop=N-vaccinated_pop-I[0]
    V=[]
    V.append(vaccinated_pop)
    S.append(unvaccinated_pop)
#creating loops for 1000 times to draw the change of infected population with time under different vaccination rates
    for i in range(1,1000):
        Time.append(i)
        #calculating the population from infected to recovered in this loop
        lis_ItoR=np.random.choice(range(2),int(I[i-1]),p=[gamma,1-gamma])
        ItoR=np.sum(lis_ItoR==0)
        proportion=I[i-1]/N
        Pinfect=proportion*beta
        #cauculating the population from susceptible to infected
        lis_StoI=np.random.choice(range(2),int(S[i-1]),p=[1-Pinfect,Pinfect])
        StoI=np.sum(lis_StoI==1)
        #append the new values in the arrays
        I.append(I[i-1]-ItoR+StoI)
        R.append(R[i-1]+ItoR)
        S.append(S[i-1]-StoI)

    #draw graph for the SIR model
    plt.plot(Time,I,label=f'{rate*100}%')

plt.legend()
plt.show()
plt.clf()