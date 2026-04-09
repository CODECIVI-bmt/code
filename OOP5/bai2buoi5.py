class NhanVien:
    def __init__(self):
        self.HoTen=[]
        self.NamSinh=[]
        self.gioitinh=[]
        self.diachi=[]
        self.HeSoLuong=[]
        self.LuongToiDa=[10]
        self.LuongTong=[]
class CongTacVien(NhanVien):
    def __init__(self):
        super().__init__()
        self.TgHoatDong=['3 thang','6 thang','1 nam']
        self.PhuCapLD=[]
    def Input(self):
        a=int(input('nhap so luong cong tac vien: '))
        for i in range(a):
            self.HoTen.append(input('nhap ho va ten: '))
            self.NamSinh.append(int(input('nhap nam sinh: ')))
            self.gioitinh.append(input('nhap gioi tinh: '))
            self.diachi.append(input('nhap dia chi: '))
            self.PhuCapLD.append(input('nhap phu cap lao dong'))
            
          
    def Output(self):
        a=input('nhap ten cong tac vien: ')
        x=int(input('nhap thoi gian hoat dong(3 tg/6 tg/1 nam): '))
        b=self.HoTen.index(a)
        if b in self.HoTen:
            print(f'ho va ten:{self.HoTen[b]}\n'
                  f'Nam sinh:{self.NamSinh[b]}\n'
                  f'dia chi :{self.diachi[b]}\n'
                  f'gioi tinh :{self.gioitinh[b]}\n'
                  f'thoi gian hoat dong :{self.TgHoatDong[x]}\n'
                  f'phu cap lao dong :{self.PhuCapLD[b]}')
class NhanVienCTG(NhanVien):
    def __init__(self):
        super().__init__(self)
        self.VitriCongViec=[]
    def Input(self):
        a=int(input('nhap so luong nhan vien: '))
        for i in range(a):
            self.HoTen.append(input('nhap ho va ten: '))
            self.NamSinh.append(int(input('nhap nam sinh: ')))
            self.gioitinh.append(input('nhap gioi tinh: '))
            self.diachi.append(input('nhap dia chi: '))
            self.VitriCongViec.append(input('nhap vi tri cong viec: '))
    def Luong(self):
     a=len(self.HoTen)
     for i in range(a):
      self.LuongTong.append(self._HeSoLuong[i]*self._LuongCoBan[i])
      self.LuongToiDa.append(self.LuongTong[i])
    def Output(self):
        a=input('nhap ten nhan vien: ')
        b=self.HoTen.index(a)
        if b in self.HoTen:
            print(f'ho va ten:{self.HoTen[b]}\n'
                  f'Nam sinh:{self.NamSinh[b]}\n'
                  f'dia chi :{self.diachi[b]}\n'
                  f'gioi tinh :{self.gioitinh[b]}\n'
                  f'vi tri cong viec :{self.VitriCongViec[b]}\n'
                  f'luong :{self.LuongTong[b]}')
class TruongPhong(NhanVien):
    def __init__(self):
        super().__init__()
        self.NgayBatDauQL=[]
        self.PhuCapQL=[]
    def Input(self):
            self.HoTen.append(input('nhap ho va ten: '))
            self.NamSinh.append(int(input('nhap nam sinh: ')))
            self.gioitinh.append(input('nhap gioi tinh: '))
            self.diachi.append(input('nhap dia chi: '))
            self.NgayBatDauQL.append(input('nhap ngay bat dau QL: '))
            self.PhuCapQL.append(input('nhap phu cap QL: '))
    def Luong(self):
     a=len(self.HoTen)
     for i in range(a):
      self.LuongTong.append((self._HeSoLuong[i]*self._LuongCoBan[i])+self.PhuCapQL[i])
      self.LuongToiDa.append(self.LuongTong[i])
    def Output(self):
        a=input('nhap ten truong phong: ')
        b=self.HoTen.index(a)
        if b in self.HoTen:
            print(f'ho va ten:{self.HoTen[b]}\n'
                  f'Nam sinh:{self.NamSinh[b]}\n'
                  f'dia chi :{self.diachi[b]}\n'
                  f'gioi tinh :{self.gioitinh[b]}\n'
                  f'vi tri cong viec :{self.VitriCongViec[b]}\n'
                  f'luong :{self.LuongTong[b]}')
   
    
        
        
        
        
        