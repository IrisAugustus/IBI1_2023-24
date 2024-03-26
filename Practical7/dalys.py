#import the modules needed for the code
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import the data being processed
os.chdir("E:/IBI1_2023-24/Practical7")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#showing the fourth column (the DALYs) from every 10th row,
#starting from the first row, for the first 100 rows (inclusive)
print(dalys_data.iloc[0:101:10,3])
#used a list of Booleans to show DALYs for all rows corresponding to Afghanistan.
rows=dalys_data.iloc[:,0]
i=[]
for name in rows:
    if name == 'Afghanistan':
        i.append(True)
    else:
        i.append(False)
print(dalys_data.iloc[i,3])

#select the data corresponding to China
s=[]
for name in rows:
    if name == 'China':
        s.append(True)
    else:
        s.append(False)
china_data=dalys_data.iloc[s,[0,2,3]]
#make seperate dataframes for Year and DALYs
china_data.DALYs=china_data.loc[:,'DALYs']
china_data.Year=china_data.loc[:,'Year']
#Compute the mean value of China DALYs data overtime
mean=np.mean(china_data.DALYs)
print('The mean value of China DALYs overtime is', mean)
#Check the DALYs data for China in 2019
print('The value of DALYs is ', china_data.DALYs.iloc[29],' in 2019.')
print('The DALYs in 2019 is below the mean value!')

#draw plots for china data, Year as the x axis, and DALYs as the Y axis
plt.figure()
plt.plot(china_data.Year, china_data.DALYs, 'bo-')
plt.xticks(china_data.Year,rotation=-90)
plt.show()
plt.clf()


