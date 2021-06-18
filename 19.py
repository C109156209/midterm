n=int(input("組數為:"))
group=[]
ans=""
for i in range(n):
    g=input("第"+str(i+1)+"組:")
    group=g.split(" ")
    total=int(group[0])*250+int(group[1])*175
    ans+="第"+str(i+1)+"組應收費用為:"+str(total) +"\n"
print(ans)