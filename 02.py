rate=int(input())
if(rate<=120):
    sm=rate*2.1
    nsm=sm
elif(rate<=330):
    sm=120*2.1+(rate-120)*3.02
    nsm=120*2.1+(rate-120)*2.68
elif(rate<=500):
    sm=120*2.1+210*3.02+(rate-330)*4.39
    nsm=120*2.1+210*2.68+(rate-330)*3.61
elif(rate<=700):
    sm=120*2.1+210*3.02+170*4.39+(rate-500)*4.97
    nsm=120*2.1+210*2.68+170*3.61+(rate-500)*4.01
else:
    sm=sm=120*2.1+210*3.02+170*4.39+200*4.97+(rate-700)*5.63
    nsm=120*2.1+210*2.68+170*3.61+200*4.01+(rate-700)*4.5
print("Summer months:"+str(round(sm,2)))
print("Non-Summer months:"+str(round(nsm,2)))
