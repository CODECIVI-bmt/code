from bai2buoi3 import Sieu_nhan
BatFamily=Sieu_nhan()

a=int(input('nhan so luong sieu nhan: '))
b=a
while(a>0):
 BatFamily.Sip(a)
 break

BatFamily.Sip_CauVong()