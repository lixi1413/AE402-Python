fo=open("波比.jpg","rb")
img=fo.read()
fo.close()
fo=open("0000.jpg","wb")
mypicture=fo.write(img)
fo.close()


