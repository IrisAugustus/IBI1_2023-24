#import necessary libraries for python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#make array of a susceptible population
population = np.zeros((100,100))
#choose a point as the outbreak point of the infection
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1\
#draw the initial image
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
#set basic values for infection
beta=0.3
gamma=0.05
m=outbreak[0]
n=outbreak[1]

#create a function to choose the eight nighbors to be infected around the infected point
def get_neighbors(x,y):
    neighbors=([x-1,y],[x-1,y-1],[x,y-1],[x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1],[x-1,y+1])
    #make sure the neighbors are present on the image
    valid_neighbors=([i,j] for i, j in neighbors if 0 <= i < population.shape[0] and 0 <= j < population.shape[1])
    return valid_neighbors

#make time loop for 100 times
for t in range(0,100):
    for x in range(0,100):
        for y in range(0,100):
            #for the points that are infected, they can infect their neighbors and recover
            if population[x,y]==1:
                infecting_neighbors= get_neighbors(x,y)
                for i,j in infecting_neighbors:
                    #if the neighbors are susceptible, randomly infect them
                    if population[i,j]==0:
                        if np.random.choice([True,False],p=[beta,1-beta]):
                            population[i,j]=1
                #decide whether infected point(x,y) will recover or not
                if np.random.choice([True,False], p=[gamma,1-gamma]):
                    population[x,y]=2
    plt.clf()
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time {t+1}')
    plt.pause(0.1)
plt.pause(5)
plt.clf()