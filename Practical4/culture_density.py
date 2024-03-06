#input initial value of culture density as a=5
#i is the number of days required for a to exceed 90
a=5
i=0
while a<=90:
    a=2*a
    i=i+1
if a>90:
    print("a=",a)
    print("after ",i," days the culture density will exceed 90")
    print("the maximum number of days you can have for a holiday is ",i-1)