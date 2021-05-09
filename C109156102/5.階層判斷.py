num=int(input("請輸入階層值 M : "))
count=1
m=1
while m<num:
    count+=1
    m=m*count
    
print(f"超過 M 為 {num} 的最小階層 N 值為 : {count}")
