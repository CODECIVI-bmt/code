from math import gcd
class Phan_So:
    def __init__(self,tu_so,mau_so):
        self.tu_so=tu_so
        self.mau_so=mau_so
    @property
    def tu_so(self):
        return self._tu_so
    @tu_so.setter
    def tu_so(self,tu):
        self._tu_so=tu
    @property
    def mau_so(self):
        return self._mau_so
    @mau_so.setter
    def mau_so(self,mau):
        if mau != 0:
            self._mau_so=mau
        else:
            raise ZeroDivisionError('thua ban roi day')
    def __add__(self,other):
        if (self._mau_so==other.mau_so):
            a=other.tu_so+self.tu_so
            b=self.mau_so
            return Phan_So(a,b).ToiGian()  
        else:
            a=(self.tu_so*other.mau_so)+(self.mau_so*other.tu_so)
            b=other.mau_so*self.mau_so
            return Phan_So(a,b).ToiGian()  
    def __sub__(self,other):
        if (self.mau_so==other.mau_so):
            a=other.tu_so-self.tu_so
            b=self.mau_so
            return Phan_So(a,b).ToiGian()  
        else:
            a=(self.tu_so*other.mau_so)-(self.mau_so*other.tu_so)
            b=other.mau_so*self.mau_so
            return Phan_So(a,b).ToiGian() 
    def __mul__(self,other):
        a=other.tu_so*self.tu_so
        b=other.mau_so*self.mau_so
        return Phan_So(a,b).ToiGian()  
    def __truediv__(self,other):
        a=self.tu_so*other.mau_so
        b=self.mau_so*other.tu_so
        return Phan_So(a,b).ToiGian() 
    def ToiGian(self):
        if (gcd(self.tu_so,self.mau_so)==1):
            return self
        else:
            a=self.tu_so//gcd(self.tu_so,self.mau_so)
            b=self.mau_so//gcd(self.tu_so,self.mau_so)
            return Phan_So(a,b).ToiGian()                 

    def __str__(self):
        return (f'{self._tu_so}/{self._mau_so}')
    def __lt__(self, other):
        return (self.tu_so * other.mau_so) < (other.tu_so * self.mau_so) 
        
def hien_thi_danh_sach(danh_sach):
    print("\n========= DANH SÁCH PHÂN SỐ =========")
    if not danh_sach:
        print("Danh sách đang trống!")
    else:
        for i, ps in enumerate(danh_sach):
            print(f"[{i + 1}] Phân số: {ps}")
    print("=====================================")

def main():
    kho_phan_so = []

    while True:
        print("\n" + "="*35)
        print(" PHẦN MỀM TÍNH TOÁN PHÂN SỐ ")
        print("="*35)
        print("1. Thêm phân số mới vào danh sách")
        print("2. Xem danh sách phân số")
        print("3. Thực hiện phép tính (+, -, *, /)")
        print("4. Sắp xếp phân số từ nhỏ đến lớn")
        print("0. Thoát chương trình")
        print("="*35)

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            print("\n--- Nhập Phân Số ---")
            try:
                tu = int(input("Nhập tử số: "))
                mau = int(input("Nhập mẫu số: "))
                ps = Phan_So(tu, mau)
                kho_phan_so.append(ps.ToiGian()) 
                print(f"Đã thêm thành công phân số: {ps.ToiGian()}")
            except ValueError:
                print(" chịu bạn rồi đấy!")
            except ZeroDivisionError as e:
                print(f" Lỗi: {e}")

        elif lua_chon == '2':
            hien_thi_danh_sach(kho_phan_so)

        elif lua_chon == '3':
            hien_thi_danh_sach(kho_phan_so)
            if len(kho_phan_so) < 2:
                print(" Cần ít nhất 2 phân số trong danh sách để tính toán!")
                continue
            
            try:
                vt1 = int(input("Chọn số thứ tự của Phân số thứ 1: ")) - 1
                vt2 = int(input("Chọn số thứ tự của Phân số thứ 2: ")) - 1
                
                ps1 = kho_phan_so[vt1]
                ps2 = kho_phan_so[vt2]

                pheptinh = input("Nhập phép tính (+, -, *, /): ")
                
                if pheptinh == '+':
                    print(f"\n Kết quả: {ps1} + {ps2} = {ps1 + ps2}")
                elif pheptinh == '-':
                    print(f"\n Kết quả: {ps1} - {ps2} = {ps1 - ps2}")
                elif pheptinh == '*':
                    print(f"\n Kết quả: {ps1} * {ps2} = {ps1 * ps2}")
                elif pheptinh == '/':
                    print(f"\n Kết quả: {ps1} / {ps2} = {ps1 / ps2}")
                else:
                    print(" Phép tính không hợp lệ!")

            except (ValueError, IndexError):
                print(" Lỗi: Số thứ tự không hợp lệ! Vui lòng nhìn kỹ danh sách.")
            except ZeroDivisionError as e:
                print(f" Lỗi chia: {e}")

        elif lua_chon == '4':
            if not kho_phan_so:
                print(" Danh sách trống")
            elif len(kho_phan_so) == 1:
                print(" Danh sách chỉ có 1 phân số!")
            else:
                kho_phan_so.sort()
                print("\n ĐÃ SẮP XẾP DANH SÁCH TỪ NHỎ ĐẾN LỚN:")
                hien_thi_danh_sach(kho_phan_so)

        elif lua_chon == '0':
            print("\n Đã thoát chương trình. Hẹn gặp lại!")
            break

        else:
            print("\n Lựa chọn không hợp lệ, vui lòng nhập từ 0 đến 4!")

if __name__ == "__main__":
    main()
     

    
    
        
            
            
        
        
    
        
        
    
    

        
        