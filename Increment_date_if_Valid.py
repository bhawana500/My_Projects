dd=int(input("Enter the Date: "))
mm=int(input("Enter the Month: "))
yy=int(input("Enter the Year: "))
print(f"Your Date is: {dd}/{mm}/{yy}")

if mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12:
    max1=31
elif mm==4 or mm==6 or mm==9 or mm==9 or mm==11:
    max1=30
elif mm==2:
    if yy%400==0:
        max1=29
    elif yy%10!=0 and yy%4==0:
        max1=29
    else:
        max1=28
k=0
if yy<1 or yy>9999 or mm<0 or mm>12:
    k=1
elif dd<1 or dd>max1:
    k=1
elif dd==max1:
    dd=1
    if mm==12:
        mm=1
        yy+=1
    else:
        mm+=1    
else:
    dd+=1  
if k==0:
    print(f"Incremented Date is: {dd}/{mm}/{yy}")
elif k==1:
    print("Invalid Date!!, Please Enter the Valid Date.")
