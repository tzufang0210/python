import random
lis=["0","1","2","3","4","5","6","7","8","9"]
Q=[]
ans=[]

Q=random.sample(lis,4)
  
while Q != ans :

    ans=input("\n"+"輸入四位數答案:")
    ans=list(ans)
    a=0
    b=0

    for x in range(0,4):
        if Q[x] == ans[x]:
            a=a+1
            

    for x in range(0,4):
        for y in range(0,4):
            if Q[x] == ans[y]:
                b=b+1            #(只看Q和ans有沒有相同,有相同b+1)
                
    b=b-a                        #(扣掉位置相同的，變成題目要求的B)

    if ans==["0","0","0","0"]:
        break


    print(str(a)+"A"+str(b)+"B")
    



