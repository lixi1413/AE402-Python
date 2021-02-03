n=int(input("請使用者輸入全班幾人"))
score=[]
highest=0
lowest=100
for i in range(n):
   mathscore=int(input("數學成績?""請先輸入最大值"))
   if highest<mathscore:
       highest=mathscore
   if lowest>mathscore:
       lowest=mathscore
   score.append(mathscore)
   print(score)
   print("最高",highest)
   print("最低",lowest)
print("結束")


