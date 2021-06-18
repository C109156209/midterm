c=input("輸入一組四位數字為:")
list1=list(c)
for i in range(len(c)):
    list1[i]=str((int(list1[i])+7)%10)
list1[0],list1[2],list1[1],list1[3]=list1[2],list1[0],list1[3],list1[1]
s=''.join(list1)
print("輸出加密後的數字為:"+s)
