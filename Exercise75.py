n = int(input("Nhập một số nguyên dương: "))
m = int(input("Nhập một số nguyên dương: "))

ucln = min(n, m)

while n % ucln != 0 or m % ucln != 0:
    ucln = ucln - 1

print("Ước chung lớn nhất của", n, "và", m, "là", ucln)
