atm=[[123,456,9000],[456,789,5000],[789,888,6000],[336,558,10000],[775,666,12000],[566,221,7000]]
n=int(input("輸入查詢組數N為:"))
user=[]
ans=""
for i in range(n):
    u=input()
    user=u.split(" ")
    if(int(user[0])==atm[i][0]):
        if(int(user[1])==atm[i][1]):
            ans+=str(atm[i][2])+"\n"
    else:
        ans+="error\n"
print(ans)