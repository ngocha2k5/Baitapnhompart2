so_thap_phan = int(input("Nhập một số thập phân: "))
ket_qua = ""

while so_thap_phan > 0:
    du = so_thap_phan % 2
    ket_qua = str(du) + ket_qua
    so_thap_phan //= 2

print("Biểu diễn nhị phân:", ket_qua)