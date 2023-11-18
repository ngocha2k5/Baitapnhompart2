print("Độ C",end="        ")
print("Độ F")
for i in range (0,101,10):
    space = ""
    
    if i < 100:
        space = " "

    if i < 10:
        space = "  "
    print (i, space ,end="        ")
    print (i*(1.8)+32)   
    
        