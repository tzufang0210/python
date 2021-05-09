c=int(input("輸入第一行正整數為 : "))
li=input("第二行中數列中的數字為 :").split(" ")

count=[]

for x in range(0,c):
    count+=[0]
    for y in li:
        if li[x]==y:
            count[x]+=1

if max(count)==0:
    print("每個數剛好只出現1次")
else:
    print(f"最大出現次數的數值為 {li[count.index(max(count))]}")
    print(f"出現的次數為 {max(count)}")


        
