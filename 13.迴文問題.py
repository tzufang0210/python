li=list(input("輸入一字元為:"))

count=[]

for x in range(0,len(li)):
    count+=[0]
    for y in li:
        if li[x]==y:
            count[x]+=1


if max(count)>1:
    print("YES")
else:
    print("NO")
