mon=int(input("小名身上有多少錢:"))
can=int(input("販賣機有幾種飲料:"))
print("",end="")
count=0
for x in range(0,can):
    sell=int(input("\n"))
    if sell<=mon:
        count+=1
print(count)
