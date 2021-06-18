s=input("輸入一整數序列為:")
s=s.split(" ")
maxc=max(s,key=s.count)
if(s.count(maxc) > len(s)/2):
    ans=maxc
else:
    ans="NO"
print("過半元素為:"+ans)