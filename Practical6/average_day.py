#import the module to be used
import matplotlib.pyplot as plt
#make the dictionary, the activity as the key, the time spent as the value
day_dir={'sleeping':8, 'classes':6, 'studying': 3.5, 'TV':2, 'music': 1, 'others': 3.5}
#This is an example for a variable for activities that can be modified, and return the correct number of hours spent on that activity
day_dir['others']=1
#restrit the sum of the values in dictionary to 24 hours
total_time=sum(day_dir.values())
if total_time > 24:
    raise ValueError("total time of the day is over 24 hours!")
print(day_dir)
#define the labels and the sizes for the pie chart
act=list(day_dir.keys())
sizes=list(day_dir.values())
#use module plt to draw the pie chart
plt.figure()
plt.title("activities in an average day")
plt.pie(sizes, labels=act, startangle=90, autopct='%.1f%%')
plt.show()
plt.clf()

#given activity: classes, and print the corresponding spent hours
print(day_dir['classes'])
