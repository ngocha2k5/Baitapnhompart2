
print("{:>4}".format(""), end="")
for i in range (1,11):
    print("{:>4}".format(i),end="")
print("")
for j in range (1,11):
    print("{:>4}".format(j), end="")
    for i in range(1, 11):
        print("{:>4}".format(i * j),end="")
        
    print("")