a=0      #暫存區
b=0      #暫存區
new=[]
ans=""
old=list(str(input("輸入四位數密碼:")))
for x in range(0,len(old)):
    new+=[(int(old[x])+7)%10]
a=new[0]
b=new[1]
new[0]=new[2]
new[1]=new[3]
new[2]=a
new[3]=b
for x in range(0,len(new)):
    ans=ans+str(new[x])
print(ans)
