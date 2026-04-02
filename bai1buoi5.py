class HangHoa:
    def __init__(self):
     self.MaHang=[]
     self.ten_hang=[]
     self.nha_sx=[]
     self.gia=[]
    
class HangDienMay(HangHoa):
    def __init__(self):
        super().__init__()
        self.tg_baohanh=[]
        self.dien_ap=[]
        self.cong_suat=[]
    def Input(self):
      a=int(input('nhap so luong hang: '))
      for i in range(a):
        self.ten_hang.append(input('nhap ten hang: '))
        self.MaHang.append(input('nhap ma hang: '))
        self.gia.append(input('nhap gia: '))
        self.nha_sx.append(input('nhap nha san xuat: '))
        self.cong_suat.append(input('nhap cong suat: '))
        self.dien_ap.append(input('nhap dien ap'))
        self.tg_baohanh.append(input('nhap thoi gian bao hanh: '))
    def Output(self):
        a=input('hay nhap ten mat hang:')
        b=self.ten_hang.index(a)
        if a in self.ten_hang:
         print(f'ten mat hang:{self.ten_hang[b]}\n'
              f'ma mat hang:{self.MaHang[b]}\n'
              f'nha san xuat:{self.nha_sx[b]}\n'
              f'gia:{self.gia[b]}\n'
              f'cong suat:{self.cong_suat[b]}\n'
              f'dien ap:{self.dien_ap[b]}\n'
              f'cong suat:{self.cong_suat[b]}\n')
        else:
            print('thua')
class HangSanhSu(HangHoa):
    def __init__(self):
        super().__init__()
        self.loai_nguyenlieu=[]
    def nhap(self):
      a=int(input('nhap so luong hang: '))
      for i in range(a):
        self.ten_hang.append(input('nhap ten hang: '))
        self.MaHang.append(input('nhap ma hang: '))
        self.gia.append(input('nhap gia: '))
        self.nha_sx.append(input('nhap nha san xuat: '))
        self.loai_nguyenlieu.append(input('nhap loai nguyen lieu: '))
    def xuat(self):
        a=input('hay nhap ten mat hang:')
        b=self.ten_hang.index(a)
        if a in self.ten_hang:
         print(f'ten mat hang:{self.ten_hang[b]}\n'
              f'ma mat hang:{self.MaHang[b]}\n'
              f'gia:{self.gia[b]}\n'
              f'nha san xuat:{self.nha_sx[b]}\n'
              f'loai nguyen lieu:{self.loai_nguyenlieu[b]}')
        else:
            print('thua')
class HangThucPham:
    def __init__(self):
        super().__init__()
        self.ngay_sx=[]
        self.ngay_hethan=[]
    def In (self):
      a=int(input('nhap so luong hang: '))
      for i in range(a):
        self.ten_hang.append(input('nhap ten hang: '))
        self.MaHang.append(input('nhap ma hang: '))
        self.gia.append(input('nhap gia: '))
        self.nha_sx.append(input('nhap nha san xuat: '))
        self.ngay_sx.append(input('nhap ngay san xuat: '))
        self.ngay_hethan.append(input('nhap ngay het han: '))
    def Out(self):
        a=input('hay nhap ten mat hang:')
        b=self.ten_hang.index(a)
        if a in self.ten_hang:
         print(f'ten mat hang:{self.ten_hang[b]}\n'
              f'ma mat hang:{self.MaHang[b]}\n'
              f'gia:{self.gia[b]}\n'
              f'nha san xuat:{self.nha_sx[b]}\n'
              f'ngay het han:{self.ngay_hethan[b]}'
              f'ngay san xuat:{self.ngay_sx[b]}')
        
a=HangDienMay()
a.Input()
a.Output()
b=HangSanhSu()
b.nhap()
b.xuat()
c=HangThucPham()
c.In()
c.Out()