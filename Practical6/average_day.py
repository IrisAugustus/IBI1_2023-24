#import the module to be used
import matplotlib.pyplot as plt
#make the dictionary, the activity as the key, the time spent as the value
day_dir={'sleeping':8, 'classes':6, 'studying': 3.5, 'TV':2, 'music': 1}
#give value to the variable "other"
day_dir['other']=input('other=')
print(day_dir)
#define the labels and the sizes for the pie chart
act=list(day_dir.keys())
sizes=list(day_dir.values())
#use module plt to draw the pie chart
plt.figure()
plt.pie(sizes, labels=act, startangle=90)
plt.show()
plt.clf()
