import math

#3
d=15*2+12*3
c=7*3+8*2+int(d/60)
e=6
f=52
if (f+c>60):
  e+=1
  f=c-(60-f)
print(e,f,sep=':')