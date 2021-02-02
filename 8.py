import random
count=0
num=random.randint(1,20)
while count<5:
    number=input("請使用者輸入1~20之間的數")
    number=int(number)
    count=count+1
    if number==num:
           print("猜中了")
           print("猜了",count,"次")          
    elif number>num:
        print("比數字小")
        print("猜了",count,"次")
    elif number<num:
        print("比數字大")
        print("猜了",count,"次")