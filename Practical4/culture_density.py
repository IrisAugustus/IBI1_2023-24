#input initial value of culture density as density=5
#day is the number of days required for density to exceed 90
#if density is over 90, break the loop, print day
density=5
day=0
while density<90:
    density=2*density
    day=day+1
if density>=90:
    print("after ",day," days the culture density will exceed 90")
    print("the maximum number of days you can have for a holiday is ",day-1)