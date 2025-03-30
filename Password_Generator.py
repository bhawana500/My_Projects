import random
def generate_password(length):
    s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRWXYZ1234567890!@#$%^&*()'
    password=''
    for i in range(length):
        password+=s[random.randint(0,len(s))]
    return password
length=int(input("Enter the number of length of your Password: "))
if length<3:
    print("Length of password should be at least 3 or more")
alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRWXYZ"
numbers="1234567890"
special_symbols='!@#$%^&*()'
password=generate_password(length)
choice=input("Do you want a strong password(Y/N): ")
if choice=='n' and length>2:
    print("Generated password is: ",password)
elif choice=='y' and length>2:
    while True:
        count=0
        count1=0
        count2=0
        for i in alphabets:
            if i in password:
                count+=1    
        for i in numbers:
            if i in password:
                count1+=1
        for i in special_symbols:
            if i in password:
                count2+=1
        if count==0 or count1==0 or count2==0:
            password=generate_password(length)
        elif count!=0 and count1!=0 and count2!=0:
            break
    print(f"Your Strong Password is: {password}")


        