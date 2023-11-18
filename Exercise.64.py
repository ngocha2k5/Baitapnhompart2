tong=0
while True:
    n=(input('Nhập giá của mặt hàng: '))
    if n=='': 
        break
    else:
        n=float(n)
    tong=tong+n
    tongdongxu=round(tong*100)
    du=tongdongxu%5
    if du==0: tongdongxuphaitra=tongdongxu
    elif du <2.5:
        tongdongxuphaitra=tongdongxu - du
    else:
        tongdongxuphaitra=tongdongxu + (5-du)
print('Tổng tiền: $', tong, sep='')
print('Số tiền thanh toán bằng tiền mặt: $',tongdongxuphaitra/100, sep='')