def days_in_month(self,m,year):
    if m==1:
        m=12
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        days=31
    elif m==4 or m==6 or m==9 or m==11:
        days=30
    elif m==2:
        if year%400==0:
            days=29
        elif year%10!=0 and year%4==0:
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
        