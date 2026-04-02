from math import *
#1
a=4/3*pi*5
print (a)
#2
b=24.95*0.4*60+24.95*60+3+0.75*59
print(b)
#3
d=15*2+12*3
c=7*3+8*2+int(d/60)
e=6
f=52
if (f+c>60):
  e+=1
  f=c-(60-f)
print(e,f,sep=':')