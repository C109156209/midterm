def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return n

num=input("請輸入正整數:")
list1=[]
for i in range(len(num)):
    for j in range(len(num),i,-1):
        list1.append(int(num[i:j]))

for k in range(len(list1)):
    list1[k]=prime(list1[k])

if(max(list1)==0):
    print("No prime found")
else:
    print(max(list1))

