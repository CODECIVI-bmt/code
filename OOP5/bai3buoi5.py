
class CanBo:
    def __init__(self, ten = "", tuoi = int, gioi_tinh = "", dia_chi = ""):
        self.__ten = ten
        self.__tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    def loaiCanBo(self):
        return "Cán Bộ"
    
    def hienThi(self):
        print(f"  Tên cán bộ        :       {self.__ten:<5}\n"
              f"  Tuổi              :       {self.__tuoi:<5}\n"
              f"  Giới tính         :       {self.__gioi_tinh:<5}\n"
              f"  Địa chỉ           :       {self.__dia_chi:<5}")
        
    def __str__(self):
        return(f"{self.loaiCanBo():<10s}   |  {self.__ten}") 
    @property
    def getTen(self):
        return self.__ten
        
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
        print(f"  Cấp Bậc           :       {self.__bac:<5}")

class KySu(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, nganh_dao_tao):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh_dao_tao = nganh_dao_tao

    def loaiCanBo(self):
        return "Kỹ Sư"

    def hienThi(self):
        kySu = " Kỹ Sư "
        print(kySu.center(36, "-"))
        super().hienThi()
        print(f"  Ngành Đào Tạo     :       {self.__nganh_dao_tao:<5}")
 
class NhanVienSX(CanBo):
    def __init__(self, ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec

    def loaiCanBo(self):
        return "Nhân Viên"

    def hienThi(self):
        nhanVien = " Nhân Viên "
        print(nhanVien.center(36, "-"))
        super().hienThi()
        print(f"  Công Việc         :       {self.__cong_viec:<5}")


class QuanLyCanBo:
    def __init__(self):
        self.__danhSachCanBo = []

    def themCanBo(self):
      try:
        print("them can bo:")
        print("1.Cong nhan")
        print("2.Ki su")
        print("3.Nhan vien")
        nghe = int(input("nhap lua chon cua ban "))
      except ValueError:
        print('nhap clgt')
       
        
        ten = input("ho va ten : ")
        tuoi = int(input("tuoi: "))
        gioi_tinh = input("gioi tinh: ")
        dia_chi = input("dia chi: ")

        if nghe == 1:
            bac = int(input("nhap cap bac (1 - 10): "))
            can_bo = CongNhan(ten, tuoi, gioi_tinh, dia_chi, bac)

        elif nghe == 2:
            nganhDTao = input("nhap nganh dao tao: ")
            can_bo = KySu(ten, tuoi, gioi_tinh, dia_chi,nganhDTao)

        elif nghe == 3:
            cViec = input("nhap cong viec: ")
            can_bo = NhanVienSX(ten, tuoi, gioi_tinh, dia_chi, cViec)
        
        self.__danhSachCanBo.append(can_bo)

    def timKiem(self):
        a = input("tim nguoi gi: ")
        b = []
        for can_bo in self.__danhSachCanBo:
            if a in can_bo.getTen:
                b.append(can_bo)

        if len(b):
            print(f" dong chi: {a}")
            for can_bo in b:
                can_bo.hienThi()

        else:
            print(f" Không tìm thấy cán bộ nào mang tên {a}")
            return
        
    def hienThongTin(self):
        if  self.__danhSachCanBo:
           try:
            for can_bo in self.__danhSachCanBo:
                can_bo.hienThi()
           except:
               print('khong biet gi het')
    def trangChu(self):
        while True:
            print("1 them nguoi dong chi")
            print("2 tim kiem anh em")
            print("3 - calling autobot")
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
    qlcb = QuanLyCanBo()
    qlcb.trangChu()