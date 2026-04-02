class Sieu_nhan():
 
    ten = []
    vu_khi = []
    mau_sac = []
        
    def Sip (self,a):
       for i in range(a):
        self.ten.append(str(input('ten la: ')))
        self.vu_khi.append(str(input('vu khi: ')))
        self.mau_sac.append(str(input('mau: ')))
    
    def Sip_CauVong(self):
        for i in range(len(self.ten)):
            print(f'ten {self.ten[i]},Cam {self.vu_khi[i]},Gao {self.mau_sac[i]}')
   
if __name__ == '__main__':
    SieuNhanGao = Sieu_nhan()
    SieuNhanGao.Sip(2)
    

   
    