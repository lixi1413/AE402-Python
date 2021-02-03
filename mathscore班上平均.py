n=int(input("請使用者輸入全班幾人"))
score=[]
name=[]
highest=0
lowest=100
highestname=""
lowestname=""
summath=0
for i in range(n):
    mathname=(input("name?"))
    mathscore=int(input("數學成績?"))
    name.append(mathname)
    score.append(mathscore)
    if highest<mathscore:
       highest=mathscore
       highestname=(mathname)
    if lowest>mathscore:
       lowest=mathscore
       lowestname=(mathname)
    summath=summath+mathscore
    score.append(mathscore)
print(score)
print("最高",highest,highestname)
print("最低",lowest,lowestname)
print("班上平均",summath/n)
print("結束")