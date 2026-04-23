import json
import os 
class CanBo:
    def __init__(self, ten = "", tuoi = int, gioi_tinh = "", dia_chi = ""):
        self._ten = ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    def loaiCanBo(self):
        return "Cán Bộ"
    
    def hienThi(self):
        print(f"  Tên cán bộ        :       {self._ten:<5}\n"
              f"  Tuổi              :       {self._tuoi:<5}\n"
              f"  Giới tính         :       {self._gioi_tinh:<5}\n"
              f"  Địa chỉ           :       {self._dia_chi:<5}")
        
    def __str__(self):
        return(f"{self.loaiCanBo():<10s}   |  {self._ten}") 
    @property
    def getTen(self):
        return self.__ten
    def to_dict(self): 
          return {
       "ho_ten": self._ten,
       "tuoi": self._tuoi,
       "gioi_tinh": self._gioi_tinh,
       "dia_chi": self._dia_chi,
       "loai": self.__class__.__name__,}
    @classmethod
    def from_dict(cls, d): 
          return cls(d["ho_ten"], d["tuoi"],
                     d["gioi_tinh"], d["dia_chi"])
        
class CongNhan(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc phải nằm trong giá trị từ 1 đến 10!")
        self.__bac = bac

    def loaiCanBo(self):
        return "Công Nhân"

    def hienThi(self):
        congNhan = " Công Nhân "
        print(congNhan.center(36, "-"))
        super().hienThi()
        print(f"  Cấp Bậc           :       {self._bac:<5}")
    def to_dict(self): 
          return {
       "ho_ten": self._ten,
       "tuoi": self._tuoi,
       "gioi_tinh": self._gioi_tinh,
       "dia_chi": self._dia_chi,
       "loai": self.__class__.__name__,
       "bac":self._bac}
    @classmethod
    def from_dict(cls, d): 
          return cls(d["ho_ten"], d["tuoi"],
                     d["gioi_tinh"], d["dia_chi"],d["bac"])

class KySu(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self._nganh_dao_tao = nganh_dao_tao

    def loaiCanBo(self):
        return "Kỹ Sư"

    def hienThi(self):
        kySu = " Kỹ Sư "
        print(kySu.center(36, "-"))
        super().hienThi()
        print(f"  Ngành Đào Tạo     :       {self._nganh_dao_tao:<5}")
    def to_dict(self): 
          return {
       "ho_ten": self._ten,
       "tuoi": self._tuoi,
       "gioi_tinh": self._gioi_tinh,
       "dia_chi": self._dia_chi,
       "loai": self.__class__.__name__,
       "nganh":self._nganh_dao_tao}
    @classmethod
    def from_dict(cls, d): 
          return cls(d["ho_ten"], d["tuoi"],
                     d["gioi_tinh"], d["dia_chi"],d["nganh"])
 
class NhanVienSX(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self._cong_viec = cong_viec

    def loaiCanBo(self):
        return "Nhân Viên"

    def hienThi(self):
        nhanVien = " Nhân Viên "
        print(nhanVien.center(36, "-"))
        super().hienThi()
        print(f"  Công Việc         :       {self._cong_viec:<5}")
    def to_dict(self): 
          return {
       "ho_ten": self._ten,
       "tuoi": self._tuoi,
       "gioi_tinh": self._gioi_tinh,
       "dia_chi": self._dia_chi,
       "loai": self.__class__.__name__,
       "cong_viec":self._cong_viec}
    @classmethod
    def from_dict(cls, d): 
          return cls(d["ho_ten"], d["tuoi"],
                     d["gioi_tinh"], d["dia_chi"],d["cong_viec"])


class QuanLyCanBo:
    def __init__(self):
       self.DanhSach=dict()
       self.Nghe=[]

    def themCanBo(self):
      try:
        print("them can bo:")
        print("1.Cong nhan")
        print("2.Ki su")
        print("3.Nhan vien")
        nghe = int(input("nhap lua chon cua ban "))
      except:
         raise ValueError('clgt')
       
        
      ten = input("ho va ten : ")
      tuoi = int(input("tuoi: "))
      gioi_tinh = input("gioi tinh: ")
      dia_chi = input("dia chi: ")

      if nghe == 1:
            bac = int(input("nhap cap bac (1 - 10): "))
            can_bo = CongNhan(ten, tuoi, gioi_tinh, dia_chi, bac)
            self.DanhSach[ten]=can_bo
            self.Nghe.append(can_bo)

      elif nghe == 2:
            nganhDTao = input("nhap nganh dao tao: ")
            can_bo = KySu(ten, tuoi, gioi_tinh, dia_chi,nganhDTao)
            self.DanhSach[ten]=can_bo
            self.Nghe.append(can_bo)

      elif nghe == 3:
            cViec = input("nhap cong viec: ")
            can_bo = NhanVienSX(ten, tuoi, gioi_tinh, dia_chi, cViec)
            self.DanhSach[ten]=can_bo
            self.Nghe.append(can_bo)
        

    def timKiem(self):
        a=input('nhap ho va ten: ')
        if a in self.DanhSach.keys():
            b=self.DanhSach.get(a)
            print(b)
    def hienThongTin(self):
        if  self.DanhSach:
           try:
            for can_bo in self.DanhSach.values():
                can_bo.hienThi()
           except:
               print('khong biet gi het')
    def trangChu(self):
        while True:
            print("1 them nguoi dong chi")
            print("2 tim kiem theo ten")
            print("3 - hien thi thong tin")
            print("0 - bye bye")

            luaChon = input("nhap lua chon cua ban: ")
            if luaChon == "1":
                self.themCanBo()
            elif luaChon == "2":
                self.timKiem()
            elif luaChon == "3":
                self.hienThongTin()
            elif luaChon == "0":
                break
            else:
                print("hay nhan lay vi huynh dai nay 1 lay!!")

if __name__ == "__main__":
    file_name="canbo.json"
    qlcb = QuanLyCanBo()
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                raw = json.load(f)
                for d in raw:
                    loai = d.get("loai")
                    if loai == "NhanVienSX":
                        cb = NhanVienSX.from_dict(d)
                    elif loai == "KySu":
                        cb = KySu.from_dict(d)
                    elif loai == "CongNhan":
                        cb = CongNhan.from_dict(d)
                    else:
                        continue
                    qlcb.DanhSach[cb.getTen] = cb
                    qlcb.Nghe.append(cb)
            except json.JSONDecodeError:
                pass
    qlcb.trangChu()
    data=[cb.to_dict() for cb in qlcb.Nghe]
    with open('canbo.json','w',encoding='utf-8') as f:
       json.dump(data, f,ensure_ascii=False, indent=2)
       
    

