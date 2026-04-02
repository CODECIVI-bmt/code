class Cho():
  ten=''
  mausac=''
  camxuc=''
  giong=''
  def Nhap(self):
    self.ten=input('nhap ten: ')
    self.mausac=input('nhap mau sac: ')
    self.camxuc=input('nhap cam xuc: ')
    self.giong=input('nhap giong: ')
  def Xuat(self):
    print(f'con cho ten {self.ten},mau {self.mausac},cam xuc {self.camxuc},giong {self.giong}')

class Oto():
    hang=''
    kichthuoc=''
    mau=''
    gia=''
    def Nhap(self):
      self.hang=input('nhap hang: ')
      self.mau=input('nhap mau sac: ')
      self.kichthuoc=input('nhap kich thuoc: ')
      self.gia=input('nhap gia: ')
    def Xuat(self):
      print(f'oto {self.hang},mau {self.mau},cam xuc {self.kichthuoc},giong {self.gia}')
class TKNH():
    TenTK=''
    SoTK=''
    NganHang=''
    SoDu=''
    def Nhap(self):
      self.TenTK=input('nhap Ten Tai Khoan: ')
      self.SoTK=int(input('nhap so tai khoan: '))
      self.NganHang=input('nhap Ngan Hang: ')
      self.SoDu=int(input('nhap So Du: '))
    def Xuat(self):
      print(f'oto {self.TenTK},mau {self.SoTK},cam xuc {self.  NganHang},giong {self.SoDu}')
     
      
a=input('nhap thu muon chon:')    
if(a==1):    
 c=['sua','vay duoi','chay','an']
 b=input('nhap phuong thuc: ')
 if b in c:
    dog=Cho()
    dog.Nhap()
    dog.Xuat()
 else:
    print('cho la ban khong la con nay')
if(a==2):
 c=['tang toc','giam toc','dam']
 b=input('nhap phuong thuc: ')
 if b in c:
     car=Oto()
     car.Nhap()
     car.Xuat()
 else:
     print('op ti mum po rai u u oe oe')
if(a==3):
 c=['rut','gui','kiem tra so du']
 b=input('nhap phuong thuc: ')
 if b in c:
     account=TKNH()
     account.Nhap()
     account.Xuat()
 else:
     print('non tk ngan hang ra!!!')
    