grades = []
tong_diem = 0
so_luong = 0

while True:
    diem_chu = input("Nhập điểm chữ (hoặc nhấn Enter để kết thúc): ")

    if diem_chu == "":
        break

    if diem_chu == "A":
        tong_diem += 4.0
    elif diem_chu == "A-":
        tong_diem += 3.7
    elif diem_chu == "B+":
        tong_diem += 3.3
    elif diem_chu == "B":
        tong_diem += 3.0
    elif diem_chu == "B-":
        tong_diem += 2.7
    elif diem_chu == "C+":
        tong_diem += 2.3
    elif diem_chu == "C":
        tong_diem += 2.0
    elif diem_chu == "C-":
        tong_diem += 1.7
    elif diem_chu == "D+":
        tong_diem += 1.3
    elif diem_chu == "D":
        tong_diem += 1.0
    elif diem_chu == "F":
        tong_diem += 0.0
    else:
        print("Điểm không hợp lệ. Vui lòng nhập một điểm chữ hợp lệ.")

    so_luong += 1

if so_luong == 0:
    print("Không có điểm nào được nhập.")
else:
    diem_tb = tong_diem / so_luong
    print("Điểm trung bình là:", round(diem_tb, 2))

    
