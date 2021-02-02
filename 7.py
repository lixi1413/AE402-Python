import random
condition=True
num=random.randint(1,20)
while condition:
    number=input("請使用者輸入1~20之間的數")
    number=int(number)
    if(number)==(num):
           print("猜中了")
           condition=False
    else:
           print("猜錯了")