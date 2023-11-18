line=input("Nhap vao 8 bit: ")
while line!="":
    if line.count("0")+line.count("1") !=8 or len(line) !=8:
        print("Day khong phai la 8 bit. Thu lai")
    else:
        ones =line.count("1")
        if ones % 2 == 0:
            print("Bit chan le phai la 0.")
        else:
            print("Bit chan le phai la 1.")
    line = input("Nhap vao 8 bit: ")