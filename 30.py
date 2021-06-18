money=int(input("小明身上有多少錢:"))
kind=int(input("販賣機有幾種飲料:"))
list1=[]
total=0
for i in range(kind):
    price=int(input())
    list1.append(price)
for i in range(kind):
    if(money>=list1[i]):
        total+=1
print(total)