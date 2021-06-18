student=[[123,"Tom","DTGD"],[456,"Cat","CSIE"],[789,"Nana","ASIE"],[321,"Lim","DBA"],[654,"Won","FDD"]]
s=int(input("輸入查詢學號為:"))
for i in range(len(student)):
    if(student[i][0]==s):
        print(str(s)+" "+student[i][1]+" "+student[i][2])