sn=input("輸入值為:").split(",")


nl=[]
for x in sn:
    nl+=[int(x)]


ma=""
mi=""
stap=nl.copy()
le=len(stap)
for x in range(0,le):
    ma+=str(max(stap))
    mi=str(max(stap))+mi
    del stap[stap.index(max(stap))]

print("最大值數列與最小值數列差值為 : "+str(int(ma)-int(mi)))
