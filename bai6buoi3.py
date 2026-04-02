class NhanVien:
  _LUONG_MAX=[10]
  _TenNhanVien=[]
  _LuongCoBan=[]
  _HeSoLuong=[]
  def SLNhanVien(self,a):
    for i in range(a):
      self._TenNhanVien.append(input('nhap ten nhan vien: '))
      self._LuongCoBan.append(float(input('nhap luong co ban: ')))
      self._HeSoLuong.append(float(input('nhap he so luong: ')))
  def TinhLuong(self,a):
    Luong=[]
    for i in range(a):
      Luong.append(self._HeSoLuong[i]*self._LuongCoBan[i])
      self._LUONG_MAX.append(Luong[i])
    for i in range(a):
      print(self._TenNhanVien[i])
      print(f'luong {Luong[i]}')
  def InTTin(self,a):
    for i in range(a):
      print(f'ten nhan vien[{i}]:{self._TenNhanVien[i]}')
      print(f'He so luong[{i}]: {self._HeSoLuong[i]}')
      print(f'Luong co ban[{i}]: {self._LuongCoBan[i]}')
  def TangLuong(self,a):
    self._LUONG_MAX.append(10)
    for i in range(1,a,1):
      if(self._LUONG_MAX[0]<self._LUONG_MAX[i]):
        return False
    return True

a=NhanVien()
b=int(input('Nhap so luong nhan vien: '))
a.SLNhanVien(b)
while(1):
  print('nhap lua chon cua ban:\n '
          '1.Tinh luong\n'
          '2.In thong tin\n'
          '3.Tang Luong\n'
          '4.bye bye\n' )
  c=int(input())
  if(c==1):
    a.TinhLuong(b)
  elif(c==2):
    a.InTTin(b)
  elif(c==3):
    print(a.TangLuong(b))
  else:
    break
  
  
