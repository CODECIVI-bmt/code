from math import *
class Circle():
    def __init__(self):
        self.x=float(input('nhap toa do x: '))
        self.y=float(input('nhap toa do y: '))
        self.radius=float(input('nhap ban kinh: '))
    def HinhTron(self):
        print(f'hinh tron co tam ({self.x},{self.y}),R={self.radius}')
    def Point_in_Circle(self):
        a=float(input('nhap toa do x cua diem A: '))
        b=float(input('nhap toa do y cua diem A: '))
        c=sqrt((a-(self.x))**2+(b-(self.y))**2)
        if(c<=self.radius):
            return True
        return False
    def RectCp_in_Circle(self):
        rx = float(input('Nhập tọa độ x của góc dưới-trái HCN: '))
        ry = float(input('Nhập tọa độ y của góc dưới-trái HCN: '))
        w = float(input('Nhập chiều rộng: '))
        h = float(input('Nhập chiều cao: '))
        corners = [
            (rx, ry),           
            (rx + w, ry),       
            (rx, ry + h),       
            (rx + w, ry + h)   
        ]
        for cx, cy in corners:
            if (cx - self.x)**2 + (cy - self.y)**2 > self.radius**2:
                return False
        return True
    def Rect_circle_overlap(self):
        i=[]
        j=[]
        for q in range(4):
            i.append(float(input(f'nhap toa do i[{q}] ')))
            j.append(float(input(f'nhap toa do j[{q}] ')))
        for k in range(4):
            if(((i[k]-self.x)**2+(j[k]-self.y)**2)<=self.radius**2):
                return True
        return  False
                
c=Circle()
while(1):
    a=int(input('lua chon y ban muon: '))
    if(a==0):
        c.HinhTron()
    if(a==1):
        c.Point_in_Circle()
    elif(a==2):
        print(c.RectCp_in_Circle())
    elif(a==3):
        print(c.Rect_circle_overlap())
    else:
        break
    



        
        
        
        
    
            
        
        
        
         
   
        