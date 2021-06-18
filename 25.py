while True:
    s=input("檢測的字串(end結束):")
    if(s=="end"):
        print("檢測結束")
        break
    s=list(s)
    c=input("檢測的單一字元:")
    print("字元%s出現的次數為:%s" %(c,str(s.count(c))))
    
