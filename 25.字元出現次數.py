while True:
    li=list(input("檢測的字串(end結束):"))
    if li==["e","n","d"]:
        break
    ck=input("檢測的單一字元:")
    count=[]

    for x in range(0,len(li)):
        count+=[0]
        for y in li:
            if li[x]==y:
                count[x]+=1


    print(f"字元 {ck} 的出現次數 {count[li.index(ck)]}")

print("測驗結束")
