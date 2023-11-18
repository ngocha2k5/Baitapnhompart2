import math

chu_vi = 0

x_dau_tien = float(input("Nhập giá trị x của tọa độ: "))
y_dau_tien = float(input("Nhập giá trị y của tọa độ: "))

x_truoc_do = x_dau_tien
y_truoc_do = y_dau_tien

while True:
    line = input("Nhập giá trị x của tọa độ (để trống để kết thúc): ")
    if line == "":
        break

    x = float(line)
    y = float(input("Nhập giá trị y của tọa độ: "))

    khoang_cach = math.sqrt((x_truoc_do - x) ** 2 + (y_truoc_do - y) ** 2)
    chu_vi += khoang_cach

    x_truoc_do = x
    y_truoc_do = y

khoang_cach_cuoi_cung = math.sqrt((x_dau_tien - x) ** 2 + (y_dau_tien - y) ** 2)
chu_vi += khoang_cach_cuoi_cung

print("Chu vi của đa giác đó là:",chu_vi)