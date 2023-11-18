pi = 0 
doidau = 1 
mauso = 1 
dem = 0 
i=0
while dem < 15:  
  t = doidau * (1 / mauso) 
  pi = pi + t
  print(i+1,") ",   4*pi, sep='')
  i=i+1
  doidau = -doidau
  mauso = mauso + 2
  dem = dem + 1