binary = list(input("Nhập số nhị phân: "))
gtri = 0
for i in range(len(binary)):
	digit = binary.pop()
	if digit == '1':
		gtri = gtri + pow(2, i)
print("Số thập phân đó là:", gtri)