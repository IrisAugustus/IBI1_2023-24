#give values to a,b,c,d,e
a=40
b=36
c=30
d=a-b
e=b-c
print('d=',d)
print('e=',e)
#make judgements whether d or e is greater
if d<e:
    print('e is greater.')
elif d==e:
    print('d equals to e.')
else:
    print('d is greater.')
# e is greater than d. 
# Using a combination of running and strength exercises to train the athletes is more effective, 
# and has a greater improvement on running time.


#3.2 Booleans exercise
X=False
Y=True
if X==Y:
    W=False
elif X!=Y:
    W=True
print("W=", W)

#The truth table of W is showed as below:
#X=True, Y=True, W=False
#X=True, Y=False, W=True
#X=False, Y=True, W=True
#X=False, Y=False, W=False