li=input("第二行中數列中的數字為 :").split(" ")

count=[]

for x in range(0,len(li)):
    count+=[0]
    for y in li:
        if li[x]==y:
            count[x]+=1


if max(count)>(len(li)/2):
    print(f"過半元素為:{li[count.index(max(count))]}")
else:
    print(f"過半元素為:NO")
