n=int(input("請輸入陣列大小:"))
list1=[]
list2=[]
total=0
position=""
for i in range(n):
    num=input()
    list1.append(list(num.split(" ")))
    for j in range(n):
        list2.append(int(list1[i][j]))
for i in range(n):
    for j in range(n):
        if(list1[i][j]==str(max(list2))):
            total+=max(list2)
            list2.remove(max(list2))
            position+="("+str(i+1)+","+str(j+1)+")"
            if(i!=n-1):
                position+=","
print("最大值為:%s\n位置為%s" %(str(total),position))
