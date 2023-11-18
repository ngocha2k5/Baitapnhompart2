tinnhan = input("Tin nhắn ban đầu:")
shift = 3

for ch in tinnhan:
    if ch.isalpha():
        vitri = ord(ch) + shift 
        if vitri > ord('z'):
                vitri -= 26
        kytu = chr(vitri)
        text = ""
        text += kytu

    print( "Tin nhắn đã chuyển đổi ", text)

