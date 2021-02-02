import random
num=random.randint(1,20)
number=input("請使用者輸入1~20之間的數")
number=int(number)
if(number)==(num):
    print("猜中了")
else:
    print("猜錯了","答案是",num)
