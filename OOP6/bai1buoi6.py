from abc import ABC,abstractmethod
class HangHoa:
    @abstractmethod
    def __init__(self):
        self._Ten_Hang=''
        self._Ma_Hang=''
        self._Nha_sx=''
        self._gia=''
    @abstractmethod
    def input(self):
       self._Ten_Hang=(input('nhap ten hang: '))
       self._Ma_Hang=(input('nhap ma hang: '))
       self._Nha_sx=(input('nhap nha san xuat: '))
       self._gia=(float(input('nhap gia:')))
       pass
    @abstractmethod
    def InTTin(self):
      pass
    @property
    def Ma_Hang(self):
      return self._Ma_Hang
    @property
    def Ten_Hang(self):
      return self._Ten_Hang
    @property
    def gia(self):
       return self._gia
    @gia.setter
    def gia(self,price):
     if isinstance(price,(int,float)) and price>0:
         self._gia=price
     else:
        raise ValueError('nhap the thi chiu roi')
class HangDienMay(HangHoa):
    def __init__(self):
        super().__init__()
        self.tg_BaoHanh=''
        self.Dien_Ap=''
        self.Cong_Suat=''
    def input(self):
         try:
            super().input()
            self.tg_BaoHanh=(input('nhap thoi gian bao hanh: '))
            self.Dien_Ap=(int(input('nhap dien ap: ')))
            self.Cong_Suat=(int(input('nhap cong suat:')))
         except:
             if not isinstance(self.gia,(int,float)):
                 raise ValueError('hay nhan lay cua toi 1 lay')
             elif not isinstance(self.Dien_Ap,(int)):
                 raise ValueError('hay nhan lay cua toi 2 lay')
             elif not isinstance(self.Cong_Suat,(int)):
                 raise ValueError('hay nhan lay cua toi 3 lay')
    def InTTin(self):
       print(f' ten san pham:{self.Ten_Hang}\n'
                f'ma san pham:{self.Ma_Hang}\n'
                f'Nha san xuat:{self.Nha_sx}\n'
                f' gia:{self.gia}\n '
                f'thoi gian bao hanh: {self.tg_BaoHanh}\n'
                f'dien ap: {self.Dien_Ap}V\n'
                f'cong suat:{self.Cong_Suat}W')
class HangSanhSu(HangHoa):
    def __init__(self):
        super().__init__()
        self.Nguyen_Lieu=''
    def input(self):
            super().input()
            self.Nguyen_Lieu=(input('nhap nguyen lieu: '))
    def InTTin(self):
       print(f' ten san pham:{self.Ten_Hang}\n'
                f'ma san pham:{self.Ma_Hang}\n'
                f'Nha san xuat:{self.Nha_sx}\n'
                f' gia:{self.gia}\n '
                f'nguyen lieu: {self.Nguyen_Lieu}\n')
class HangThucPham(HangHoa):
    def __init__(self):
        super().__init__()
        self.Ngay_San_Xuat=''
        self.Ngay_Het_Han=''
    def input(self):
            super().input()
            self.Ngay_San_Xuat=(input('ngay san xuat: '))
            self.Ngay_Het_Han=(input('nhap ngay het han: '))
    def InTTin(self):
       print(f' ten san pham:{self.Ten_Hang}\n'
                f'ma san pham:{self.Ma_Hang}\n'
                f'Nha san xuat:{self.Nha_sx}\n'
                f' gia:{self.gia}\n '
                f'ngay san xuat: {self.Ngay_San_Xuat}'
                )
       if __name__ == '__main__':
         kho_hang=[]
         while True:
          print("1. them mat hang dien may")
          print("2. them mat hang sanh su")
          print("3. them mat hang thuc pham")
          print("4. hien thi toan bo kho hang")
          print("0. thoat chuong trinh")
          lua_chon = input("nhap lua chon cua ban (0-4): ")
          if lua_chon == '1':
            sp = HangDienMay()      
            sp.input()               
            kho_hang.append(sp)      
          elif lua_chon == '2':
            sp = HangSanhSu()
            sp.input()
            kho_hang.append(sp)
          elif lua_chon == '3':
            sp = HangThucPham()
            sp.input()
            kho_hang.append(sp)
          elif lua_chon == '4':
            if not kho_hang:
                print("co cai nit")
            else:
                for sp in kho_hang:
                    sp.InTTin()
          elif lua_chon == '0':
            print("\n bye bye")
            break  
          else:
            print("nhap cai gi vay")