def days_in_month(m,y):
    m1=int(m)-1
    if m1==0:
        m1=12
    if m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10 or m1==12:
        days=31
    elif m1==4 or m1==6 or m1==9 or m1==11:
        days=30
    elif m1==2:
        if y%400==0 or (y%100!=0 and y%4==0):
            days=29
        else:
            days=28
    return days 
import datetime
dd=int(input("Enter the Date: "))
mm=int(input("Enter the Month: "))
yy=int(input("Enter the Year: "))
now=datetime.datetime.now()
y=now.strftime("%Y")
m=now.strftime("%m")
d=now.strftime("%d")
year=int(y)-yy
month=int(m)-mm
date=int(d)-dd
if month<0:
    month+=12
    year-=1
if date<0:
    month-=1
    date+=days_in_month(m,y)
print(f"You are {year} years, {month} months and {date} days old. ")
        