li=input("").split(" ")
lis=[]
for x in li:
    
    if x=="A":
        lis+=[1]
        continue;
    if x=="J":
        lis+=[11]
        continue;    
    if x=="Q":
        lis+=[12]
        continue;
    if x=="K":
        lis+=[13]
        continue;
    lis+=[int(x)]

print(lis)
print(sum(lis))
    
