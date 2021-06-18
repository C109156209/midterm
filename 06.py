n=input("輸入值為:")
list1=n.split(",")
list1=sorted(list1)
a=""
for i in range(len(list1)):
    a+=list1[i]
print("最大值數列與最小值數列差為:"+str(int(a[::-1])-int(a)))
