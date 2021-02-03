n=int(input("請使用者輸入全班幾人"))
score=[]
highest=0
lowest=100
highestname=""
lowestname=""
summath=0
for i in range(0,2*n):
    mathscore=input("輸入")
    score.append(mathscore)
    print(score)
    if i%2==1:
        score[i]=int(score[i])
        summath=summath+score[i]
        score.append(mathscore)
        if highest<score[i]:
            higest=score[i]
        if lowest>score[i]:
            lowest=score[i]
print(score)
print("最高",highest,highestname)
print("最低",lowest,lowestname)
print("班上平均",summath/n)
print("結束")