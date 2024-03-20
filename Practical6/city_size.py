#import the module to be used
import numpy as np
import matplotlib.pyplot as plt

#iput different populations of cities, using lists
uk_pop=[0.56,0.62,0.04,9.7]
cn_pop=[0.58,8.4,29.9,22.2]
#count the number of the cities
num_uk=len(uk_pop)
num_cn=len(cn_pop)
#sort the population in the list
uk_pop.sort()
cn_pop.sort()
print("uk:",uk_pop)
print("cn:",cn_pop)
#adding the city names into lists
name_uk=['Stirling', 'Edinburgh', 'Glasgow', 'London']
name_cn=['Haining', 'Hangzhou', 'Beijing', 'Shanghai']
#set the basic values for the graphs
width=0.5
ind_uk=name_uk
ind_cn=name_cn

#draw the bar chart for uk
plt.figure()
plt.bar(ind_uk, uk_pop, width, color="blue")
plt.ylabel('population (million)')
plt.title('population of different UK cities')
plt.xticks(ind_uk)
plt.show()
plt.clf()

#draw the bar chart for cn
plt.bar(ind_cn, cn_pop, width, color="pink")
plt.ylabel('population (million)')
plt.title('population of different CN cities')
plt.xticks(ind_cn)
plt.show()
plt.clf()
