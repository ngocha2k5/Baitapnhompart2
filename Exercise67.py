s = 0
while True:
    n=input("Nhập độ tuổi: ")
    if n!="" and n.isnumeric():
        age = int(n)
        if age<=2:
            s= s + 0
        elif 3<=age<=12:
            s= s + 14
        elif age>=65:
            s= s + 18
        else:
            s= s + 23
        
    else:
        break
print("Tong tien la:",s)
        
     
    