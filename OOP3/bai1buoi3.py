from math import *
class Point() :
    x=int
    y=int
    def diemB (self): 
       self.x=int(input('nhap toa do x: '))
       self.y=int(input('nhap toa do y: '))
       print (f'toa do B:({self.x},{self.y})')
    
    def diemA (self):
       print (f'toa do A: (3,4)')
   
    def getX (self):
        return self.x*-1
   
    def getY (self):
        return self.y*-1
    
    def Distance1(self):
        a=sqrt((self.x-3)**2+(self.y-4)**2)
        print(a)
    def Distance2(self):
        a=sqrt((self.x)**2+(self.y)**2)
        print(a)    
    
a=Point()

while(1):
 choice=int(input('chon cau so may?? '))
 if(choice==1):
    a.diemA()
 elif(choice==2):
    a.diemB()
 elif(choice==3):
    print(f'toa do diem C: ({a.getX()},{a.getY()})') 
 elif(choice==4):
    a.Distance2()
 elif(choice==5):
    a.Distance1()
   
    
    
    





    
  
    
   






       
