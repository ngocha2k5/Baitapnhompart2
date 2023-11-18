n = int(input("Nhập số: "))
for i in range(2,n + 1):
    if n % i == 0:
        dem = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                dem = 0
                break
        if(dem == 1):
            print(i)