while True:
    input_str = input("Nhập chuỗi (nhấn Enter để thoát): ")
    
    if not input_str:
        break
    
    clean_str = ''.join(input_str.split()).lower()
    
    if clean_str == clean_str[::-1]:
        print(input_str, "là palindrome.")
    else:
        print(input_str, "không là palindrome.")