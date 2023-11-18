print("{:<15} {:<15} {:<15}".format("Gia goc", "Giam gia", "Gia moi"))
originPrice=[4.95, 9.95, 14.95, 24.95]

discountPercent = 0.6

for i in range(0, len(originPrice)):
    discountAmount = round(originPrice[i] * discountPercent, 2)
    
    newPrice = round(originPrice[i] - discountAmount, 2)
    print("{:<15} {:<15} {:<15}".format(originPrice[i], discountAmount, newPrice))
    


