n=int(input("測試的資料量:"))
blood=[]
ans=""
for i in range(n):
    b=input()
    blood=b.split(" ")
    n-=1
    if(blood[2]=="A"):
        if(blood[0]=="A" or blood[1]=="A" or blood[0]=="AB" or blood[1]=="AB"):
            ans+="YES\n"
        else:
            ans+="IMPOSSIBLE\n"
    if(blood[2]=="B"):
        if(blood[0]=="B" or blood[1]=="B" or blood[0]=="AB" or blood[1]=="AB"):
                ans+="YES"
        else:
            ans+="IMPOSSIBLE\n"
    if(blood[2]=="AB"):
        if(blood[0]=="AB" or blood[1]=="AB"):
            ans+="YES"
        else:
            ans+="IMPOSSIBLE\n"
    if(blood[2]=="O"):
        if(blood[0]!="AB" or blood[1]!="AB"):
            ans+="YES"
        else:
            ans+="IMPOSSIBLE\n"
print(ans)