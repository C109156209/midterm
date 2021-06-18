n=input("輸入第一行正整數為:")
while True:
    s=input("第二行中數列的數字為:")
    if(len(s)==((int(n)*2)-1)):
        break
    else:
        continue
s=s.split(" ")
maxc=max(s,key=s.count)
if(maxc==1):
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為:"+str(maxc))
    print("出現次數:"+str(s.count(maxc)))
