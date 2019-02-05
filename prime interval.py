for num in range(100,200):
    h=0
    for i in range(1,200+1):
        if (num%i==0):
            h=h+1
    if(h==2):
 	print num
