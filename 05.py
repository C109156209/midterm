M=int(input("請輸入階乘值M:"))
N=1
total=1
while(total<=M):
    N+=1
    total*=N
print("超過M為%s的最小階乘N值為:%s" %(M,N))